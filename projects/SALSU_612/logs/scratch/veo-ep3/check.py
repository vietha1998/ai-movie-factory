import build, sys
sc = build.parse_script()
authored = build.load_batches()
recs = [build.build_scene(s, sc[s["id"]]) for s in authored]
recs.sort(key=lambda r: r["id"])
errs = [e for e in build.validate(recs) if not e.startswith("ID mismatch") and not e.startswith("total seconds") and "t_start" not in e]
print(len(recs), "SC authored;", len(errs), "errors")
for e in errs: print(" ", e)
ids = [r["id"] for r in recs]
print("last:", ids[-1])
if "--show" in sys.argv:
    r = recs[int(sys.argv[sys.argv.index("--show")+1])]
    import json; print(json.dumps({k: r[k] for k in ("id","image_prompt","refs","video_prompt")}, ensure_ascii=False, indent=1))
