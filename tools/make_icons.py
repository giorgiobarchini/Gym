#!/usr/bin/env python3
"""Genera los íconos de la app en docs/icons (pesa lima sobre fondo oscuro)."""
import pathlib
from PIL import Image, ImageDraw

OUT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "icons"
OUT.mkdir(parents=True, exist_ok=True)
BG, LIME = (17, 19, 16), (200, 245, 58)

def icon(size, safe=1.0, rounded=True):
    s = 4  # supersampling
    W = size * s
    im = Image.new("RGB", (W, W), BG)
    d = ImageDraw.Draw(im)
    c, u = W / 2, W * 0.36 * safe  # u = media anchura del dibujo
    def R(x0, y0, x1, y1, r):
        d.rounded_rectangle([c + x0 * u, c + y0 * u, c + x1 * u, c + y1 * u], radius=r * u, fill=LIME)
    R(-0.62, -0.09, 0.62, 0.09, 0.05)      # barra
    R(-0.92, -0.42, -0.70, 0.42, 0.08)     # disco grande izq
    R(-0.66, -0.30, -0.48, 0.30, 0.07)     # disco chico izq
    R(0.70, -0.42, 0.92, 0.42, 0.08)       # disco grande der
    R(0.48, -0.30, 0.66, 0.30, 0.07)       # disco chico der
    im = im.resize((size, size), Image.LANCZOS)
    return im

icon(512).save(OUT / "icon-512.png")
icon(192).save(OUT / "icon-192.png")
icon(180).save(OUT / "apple-touch-icon.png")
icon(512, safe=0.75).save(OUT / "icon-maskable-512.png")
print("íconos listos")
