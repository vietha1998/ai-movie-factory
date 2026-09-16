#!/usr/bin/env python3
"""
G-Labs Automation webhook client — submit → poll → download.
Dùng chung cho toàn pipeline (character refs, location refs, scene images, scene videos, upscale).

Usage (CLI):
  python3 tools/glabs_client.py health
  python3 tools/glabs_client.py image  --prompt "..." --out dir/ [--ref path.png ...] [--ar 16:9] [--model nano_banana_pro] [--upscale 2K]
  python3 tools/glabs_client.py video  --prompt "..." --out dir/ [--start path.png] [--ref path.png ...] [--len 8] [--res 1080p] [--model veo_31_fast]
  python3 tools/glabs_client.py upscale --image path.png --out dir/ [--scale 4]
  python3 tools/glabs_client.py batch  --jobs jobs.json --out dir/ [--parallel 4]
  python3 tools/glabs_client.py resume --jobs jobs.json --out dir/   # chạy lại job chưa có file

jobs.json: [{"id":"SC_001","type":"image|video","body":{...}, "chain_from":"SC_000"(tùy chọn)}, ...]
  chain_from: lấy frame cuối video của job đó làm start_image (tail-frame continuity, học từ novelvids)
Kết quả ghi vào <out>/<id>_<n>.<ext> và <out>/glabs_results.jsonl
"""
import argparse, base64, json, mimetypes, os, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / "config" / "glabs.env"


def load_env():
    cfg = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            cfg[k.strip()] = v.strip()
    cfg.setdefault("GLABS_BASE_URL", os.environ.get("GLABS_BASE_URL", "http://127.0.0.1:8765"))
    cfg.setdefault("GLABS_API_KEY", os.environ.get("GLABS_API_KEY", ""))
    cfg.setdefault("GLABS_IMAGE_MODEL", "nano_banana_pro")
    cfg.setdefault("GLABS_VIDEO_MODEL", "veo_31_fast")
    cfg.setdefault("GLABS_VIDEO_RESOLUTION", "1080p")
    cfg.setdefault("GLABS_POLL_SECONDS", "4")
    cfg.setdefault("GLABS_TIMEOUT_SECONDS", "900")
    return cfg


CFG = load_env()
BASE = CFG["GLABS_BASE_URL"].rstrip("/")
HDR = {"X-API-Key": CFG["GLABS_API_KEY"], "Content-Type": "application/json"}


class GLabsError(RuntimeError):
    pass


def _req(method, path, body=None, auth=True, timeout=60):
    url = BASE + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    if auth:
        for k, v in HDR.items():
            req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try:
            msg = e.read().decode()
        except Exception:
            msg = str(e)
        raise GLabsError(f"HTTP {e.code} {path}: {msg}")
    except urllib.error.URLError as e:
        raise GLabsError(f"G-Labs không phản hồi tại {BASE} ({e.reason}). Mở app G-Labs và bật tab Webhook.")


def health():
    return _req("GET", "/api/health", auth=False, timeout=5)


def ref_obj(path, name=None, category="subject"):
    """Ref image object. Cùng máy → dùng path tuyệt đối (không cần base64)."""
    p = Path(path).resolve()
    if not p.exists():
        raise FileNotFoundError(p)
    return {"path": str(p), "name": name or p.stem, "category": category}


def ref_b64(path):
    p = Path(path)
    mime = mimetypes.guess_type(str(p))[0] or "image/png"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()


def submit(endpoint, body):
    r = _req("POST", f"/api/{endpoint}/generate", body)
    if "task_id" not in r:
        raise GLabsError(f"Không nhận được task_id: {r}")
    return r["task_id"]


def poll(task_id, poll_s=None, timeout_s=None):
    poll_s = float(poll_s or CFG["GLABS_POLL_SECONDS"])
    timeout_s = float(timeout_s or CFG["GLABS_TIMEOUT_SECONDS"])
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        s = _req("GET", f"/api/status/{task_id}")
        st = s.get("status")
        if st == "completed":
            return s.get("results", [])
        if st == "failed":
            raise GLabsError(f"[{s.get('error_code')}] {s.get('error')} | {s.get('error_detail','')}")
        time.sleep(poll_s)
    raise GLabsError(f"Task {task_id} timeout sau {timeout_s}s")


def extract_last_frame(video_path, out_png=None):
    """Trích frame cuối clip (ffmpeg) → dùng làm start_image cho clip kế tiếp (tail-frame continuity)."""
    import subprocess
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from ffbin import ffmpeg_path
    video_path = Path(video_path)
    out_png = Path(out_png) if out_png else video_path.with_name(video_path.stem + "_last.png")
    cmd = [ffmpeg_path(), "-y", "-loglevel", "error", "-sseof", "-0.2", "-i", str(video_path), "-frames:v", "1", "-q:v", "2", str(out_png)]
    subprocess.run(cmd, check=True)
    return out_png


def download(url, dest):
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=300) as r:
        dest.write_bytes(r.read())
    return dest


def run_job(job_id, endpoint, body, out_dir, retries=2):
    """Submit + poll + download. Retry khi 429 (quota) với backoff."""
    out_dir = Path(out_dir)
    attempt = 0
    t0 = time.time()
    while True:
        attempt += 1
        try:
            tid = submit(endpoint, body)
            urls = poll(tid)
            files = []
            for i, u in enumerate(urls, 1):
                ext = os.path.splitext(u.split("?")[0])[1] or (".mp4" if endpoint == "video" else ".png")
                files.append(str(download(u, out_dir / f"{job_id}_{i}{ext}")))
            rec = {"id": job_id, "type": endpoint, "task_id": tid, "status": "completed", "files": files, "ts": time.time(),
                   "model": body.get("model"), "resolution": body.get("resolution"), "seconds": body.get("video_length"),
                   "elapsed_s": round(time.time() - t0, 1)}
            _log(out_dir, rec)
            return rec
        except GLabsError as e:
            msg = str(e)
            if "[429]" in msg and attempt <= retries:
                wait = 60 * attempt
                print(f"[{job_id}] quota 429 → đợi {wait}s rồi thử lại ({attempt}/{retries})", file=sys.stderr)
                time.sleep(wait)
                continue
            rec = {"id": job_id, "type": endpoint, "status": "failed", "error": msg, "ts": time.time()}
            _log(out_dir, rec)
            return rec


def _log(out_dir, rec):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    with open(Path(out_dir) / "glabs_results.jsonl", "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


# ---------- body builders (pipeline dùng trực tiếp) ----------
def image_body(prompt, refs=(), ar="16:9", model=None, upscale=()):
    return {
        "prompt": prompt,
        "model": model or CFG["GLABS_IMAGE_MODEL"],
        "aspect_ratio": ar,
        "reference_images": [ref_obj(r) if isinstance(r, str) else r for r in refs][:10],
        "upscale": list(upscale),
    }


def video_body(prompt, start_image=None, refs=(), length=8, res=None, model=None, ar="16:9"):
    body = {
        "prompt": prompt,
        "model": model or CFG["GLABS_VIDEO_MODEL"],
        "aspect_ratio": ar,
        "resolution": [res or CFG["GLABS_VIDEO_RESOLUTION"]],
        "video_length": int(length),
    }
    imgs = []
    if start_image:
        body["mode"] = "start_image"
        imgs.append(ref_obj(start_image, name="start"))
    else:
        body["mode"] = "components" if refs else "text_to_video"
    imgs += [ref_obj(r) if isinstance(r, str) else r for r in refs]
    body["reference_images"] = imgs[:3]
    return body


def upscale_body(image_path, scale=4, model=None):
    b = {"image_path": str(Path(image_path).resolve()), "scale": int(scale)}
    if model:
        b["model"] = model
    return b


# ---------- CLI ----------
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("health")

    p = sub.add_parser("image"); p.add_argument("--prompt", required=True); p.add_argument("--out", required=True)
    p.add_argument("--ref", action="append", default=[]); p.add_argument("--ar", default="16:9")
    p.add_argument("--model"); p.add_argument("--upscale", action="append", default=[]); p.add_argument("--id", default="img")

    p = sub.add_parser("video"); p.add_argument("--prompt", required=True); p.add_argument("--out", required=True)
    p.add_argument("--start"); p.add_argument("--ref", action="append", default=[]); p.add_argument("--len", type=int, default=8)
    p.add_argument("--res"); p.add_argument("--model"); p.add_argument("--id", default="vid")

    p = sub.add_parser("upscale"); p.add_argument("--image", required=True); p.add_argument("--out", required=True)
    p.add_argument("--scale", type=int, default=4); p.add_argument("--model"); p.add_argument("--id", default="up")

    for name in ("batch", "resume"):
        p = sub.add_parser(name); p.add_argument("--jobs", required=True); p.add_argument("--out", required=True)
        p.add_argument("--parallel", type=int, default=4)

    a = ap.parse_args()
    if a.cmd == "health":
        print(json.dumps(health(), indent=2)); return
    if a.cmd == "image":
        print(json.dumps(run_job(a.id, "image", image_body(a.prompt, a.ref, a.ar, a.model, a.upscale), a.out), ensure_ascii=False)); return
    if a.cmd == "video":
        print(json.dumps(run_job(a.id, "video", video_body(a.prompt, a.start, a.ref, a.len, a.res, a.model), a.out), ensure_ascii=False)); return
    if a.cmd == "upscale":
        print(json.dumps(run_job(a.id, "upscale", upscale_body(a.image, a.scale, a.model), a.out), ensure_ascii=False)); return
    if a.cmd in ("batch", "resume"):
        jobs = json.loads(Path(a.jobs).read_text())
        out = Path(a.out)
        if a.cmd == "resume":  # bỏ qua job đã có file kết quả
            done = set()
            lf = out / "glabs_results.jsonl"
            if lf.exists():
                for line in lf.read_text().splitlines():
                    try:
                        r = json.loads(line)
                        if r.get("status") == "completed" and all(Path(f).exists() for f in r.get("files", [])):
                            done.add(r["id"])
                    except Exception:
                        pass
            jobs = [j for j in jobs if j["id"] not in done]
            print(f"resume: {len(done)} đã xong, {len(jobs)} còn lại")
        # chain: job có "chain_from": "<id>" → chờ job đó xong, lấy frame cuối làm start_image
        chained = [j for j in jobs if j.get("chain_from")]
        free = [j for j in jobs if not j.get("chain_from")]
        results, files_by_id = [], {}
        def _run(j):
            return run_job(j["id"], j["type"], j["body"], out)
        with ThreadPoolExecutor(max_workers=a.parallel) as ex:
            futs = {ex.submit(_run, j): j["id"] for j in free}
            for f in as_completed(futs):
                r = f.result(); results.append(r)
                if r["status"] == "completed": files_by_id[r["id"]] = r["files"]
                print(f"[{r['id']}] {r['status']}" + (f" → {r.get('files')}" if r['status']=='completed' else f" ✗ {r.get('error')}"))
        # chained jobs chạy tuần tự theo thứ tự trong file
        for j in chained:
            src = files_by_id.get(j["chain_from"])
            if not src:
                # thử tìm file có sẵn từ lô trước
                cand = sorted(out.glob(f"{j['chain_from']}_*.mp4"))
                src = [str(cand[-1])] if cand else None
            if not src:
                r = {"id": j["id"], "type": j["type"], "status": "failed", "error": f"chain_from {j['chain_from']} chưa có video", "ts": time.time()}
                _log(out, r); results.append(r); print(f"[{j['id']}] ✗ {r['error']}"); continue
            tail = extract_last_frame(src[0], out / f"{j['id']}_start_from_{j['chain_from']}.png")
            body = dict(j["body"]); body["mode"] = body.get("mode", "start_image")
            body["reference_images"] = [ref_obj(tail, name="start")] + [x for x in body.get("reference_images", []) if not (isinstance(x, dict) and x.get("name") == "start")]
            body["reference_images"] = body["reference_images"][:3]
            r = run_job(j["id"], j["type"], body, out); results.append(r)
            if r["status"] == "completed": files_by_id[r["id"]] = r["files"]
            print(f"[{r['id']}] {r['status']} (chained from {j['chain_from']})" + (f" → {r.get('files')}" if r['status']=='completed' else f" ✗ {r.get('error')}"))
        ok = sum(1 for r in results if r["status"] == "completed")
        print(f"\nDONE {ok}/{len(results)} completed")


if __name__ == "__main__":
    try:
        main()
    except GLabsError as e:
        print(f"GLABS_ERROR: {e}", file=sys.stderr); sys.exit(2)
