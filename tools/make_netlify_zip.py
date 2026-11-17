#!/usr/bin/env python3
"""Arma docs/ y lo empaqueta en gym-netlify.zip para subir a Netlify arrastrando (sin GitHub)."""
import pathlib, subprocess, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
subprocess.run([sys.executable, str(ROOT / "tools" / "build_pages.py")], check=True)
src = ROOT / "docs"
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "gym-netlify.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(src.rglob("*")):
        if f.is_file() and f.name != ".nojekyll":
            z.write(f, pathlib.Path("gym") / f.relative_to(src))
print("listo:", out)
