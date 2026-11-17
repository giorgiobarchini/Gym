#!/usr/bin/env python3
"""Arma la versión instalable (GitHub Pages) en docs/ a partir de index.html.

index.html es la fuente única: se publica tal cual como Artifact de Claude, y este
script le agrega el esqueleto HTML, el manifest, los íconos y Supabase.
Uso:  python3 tools/build_pages.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
OUT.mkdir(exist_ok=True)

page = (ROOT / "index.html").read_text(encoding="utf-8")
page = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?', "", page)

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Gym">
<meta name="theme-color" content="#111310">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px/1.4 system-ui,-apple-system,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
<script src="config.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.js"></script>
</head>
<body>
"""
(OUT / "index.html").write_text(HEAD + page + "\n</body>\n</html>\n", encoding="utf-8")

(OUT / "manifest.webmanifest").write_text("""{
  "name": "Cuaderno de Gym",
  "short_name": "Gym",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait",
  "background_color": "#111310",
  "theme_color": "#111310",
  "lang": "es",
  "icons": [
    { "src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ]
}
""", encoding="utf-8")

cfg = OUT / "config.js"
if not cfg.exists():
    cfg.write_text("""// Datos de tu proyecto de Supabase (Project Settings → API).
// La clave "anon" / "publishable" es pública por diseño: tus datos los protegen las reglas (RLS) de la tabla.
// NUNCA pongas acá la clave "service_role" / "secret".
window.GYM_CONFIG = {
  supabaseUrl: "",
  supabaseKey: ""
};
""", encoding="utf-8")
(OUT / ".nojekyll").write_text("")
print("docs/ listo")
