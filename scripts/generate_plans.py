#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_plans.py — Generador de planos CAD/PDF para muebles y estructuras.

Uso:
  python generate_plans.py input.json --out ./salida

Input JSON (ejemplo en example_input.json):
  {
    "project": "estante-madera",
    "units": "mm",
    "parts": [
      {"name": "Estante", "dims": [1000, 250, 18], "pos": [0, 0, 0], "material": "Melamina"}
    ]
  }
  dims = [Largo, Ancho, Alto] (X, Y, Z)
  pos  = [x, y, z] esquina inferior-izquierda-posterior

Salida:
  <project>.dxf  (vistas ortogonales + explosionada, con cotas)
  <project>.svg  (vistas ortogonales + explosionada)
  <project>.pdf  (plano completo con vistas y cotas)
"""

import argparse
import json
import os
import math

import ezdxf
from ezdxf import units as ezunits
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.units import mm as rl_mm


# ---------- Geometria ----------

def bbox(part):
    x, y, z = part["pos"]
    L, W, H = part["dims"]
    return (x, y, z, x + L, y + W, z + H)


def overall(parts):
    xs = [b[0] for b in [bbox(p) for p in parts]] + [b[3] for b in [bbox(p) for p in parts]]
    ys = [b[1] for b in [bbox(p) for p in parts]] + [b[4] for b in [bbox(p) for p in parts]]
    zs = [b[2] for b in [bbox(p) for p in parts]] + [b[5] for b in [bbox(p) for p in parts]]
    return (min(xs), min(ys), min(zs), max(xs), max(ys), max(zs))


# ---------- Proyecciones 2D ----------

def proj_top(parts):
    # vista superior: X (horizontal) vs Y (vertical)
    out = []
    for p in parts:
        x0, y0, z0, x1, y1, z1 = bbox(p)
        out.append((p["name"], x0, y0, x1 - x0, y1 - y0))
    return out


def proj_front(parts):
    # vista frontal: X (horizontal) vs Z (vertical)
    out = []
    for p in parts:
        x0, y0, z0, x1, y1, z1 = bbox(p)
        out.append((p["name"], x0, z0, x1 - x0, z1 - z0))
    return out


def proj_right(parts):
    # vista lateral derecha: Y (horizontal) vs Z (vertical)
    out = []
    for p in parts:
        x0, y0, z0, x1, y1, z1 = bbox(p)
        out.append((p["name"], y0, z0, y1 - y0, z1 - z0))
    return out


def proj_bottom(parts):
    # vista inferior: X vs Y (igual a top, se dibuja invertida en Y para convencion)
    out = []
    for p in parts:
        x0, y0, z0, x1, y1, z1 = bbox(p)
        out.append((p["name"], x0, y0, x1 - x0, y1 - y0))
    return out


def iso_point(x, y, z):
    # proyeccion isometrica simple
    return (x - y, (x + y) * 0.5 + z)


def proj_iso(parts, explode=0.0):
    # vista explosionada: separar cada pieza radialmente desde el centroide general
    ox0, oy0, oz0, ox1, oy1, oz1 = overall(parts)
    cx, cy, cz = (ox0 + ox1) / 2, (oy0 + oy1) / 2, (oz0 + oz1) / 2
    out = []
    for p in parts:
        x0, y0, z0, x1, y1, z1 = bbox(p)
        pcx, pcy, pcz = (x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2
        dx, dy, dz = pcx - cx, pcy - cy, pcz - cz
        n = math.sqrt(dx * dx + dy * dy + dz * dz) or 1.0
        if explode > 0:
            sx = dx / n * explode
            sy = dy / n * explode
            sz = dz / n * explode
        else:
            sx = sy = sz = 0.0
        # 8 vertices del cubo desplazados
        verts = []
        for (xx, yy, zz) in [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
                              (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]:
            ix, iy = iso_point(xx + sx, yy + sy, zz + sz)
            verts.append((ix, iy))
        out.append((p["name"], verts, (x0 + sx, y0 + sy, z0 + sz, x1 + sx, y1 + sy, z1 + sz),
                    (pcx, pcy, pcz), (pcx + sx, pcy + sy, pcz + sz)))
    return out


# ---------- DXF ----------

def make_dxf(parts, units, project, outdir):
    doc = ezdxf.new("R2010")
    doc.units = ezunits.MM if units == "mm" else ezunits.IN
    msp = doc.modelspace()

    # capas
    for layer in ["TOP", "FRONT", "RIGHT", "BOTTOM", "ISO", "DIM", "TEXT"]:
        if layer not in doc.layers:
            doc.layers.add(layer)

    gap = 200.0  # separacion entre vistas
    ox0, oy0, oz0, ox1, oy1, oz1 = overall(parts)
    W = ox1 - ox0
    D = oy1 - oy0
    H = oz1 - oz0

    # Helper para dibujar rectangulo
    def rect(msp, x, y, w, h, layer):
        pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": layer})

    def text(msp, x, y, s, layer="TEXT", height=5):
        msp.add_text(s, dxfattribs={"insert": (x, y), "height": height, "layer": layer})

    def dim_horizontal(msp, x0, y, x1, layer="DIM", offset=10):
        # linea de cota horizontal con extensiones
        yd = y - offset
        msp.add_line((x0, y), (x0, yd), dxfattribs={"layer": layer})
        msp.add_line((x1, y), (x1, yd), dxfattribs={"layer": layer})
        msp.add_line((x0, yd), (x1, yd), dxfattribs={"layer": layer})
        msp.add_text(f"{x1-x0:.0f}", dxfattribs={"insert": ((x0+x1)/2, yd-4), "height": 4, "layer": layer})

    def dim_vertical(msp, x, y0, y1, layer="DIM", offset=10):
        xd = x + offset
        msp.add_line((x, y0), (xd, y0), dxfattribs={"layer": layer})
        msp.add_line((x, y1), (xd, y1), dxfattribs={"layer": layer})
        msp.add_line((xd, y0), (xd, y1), dxfattribs={"layer": layer})
        msp.add_text(f"{y1-y0:.0f}", dxfattribs={"insert": (xd+2, (y0+y1)/2), "height": 4, "layer": layer, "rotation": 90})

    # --- Vista superior (top) ---
    base_x, base_y = 0, 0
    for name, x, y, w, h in proj_top(parts):
        rect(msp, base_x + (x - ox0), base_y + (y - oy0), w, h, "TOP")
    text(msp, base_x, base_y + D + 10, "VISTA SUPERIOR", "TEXT", 6)
    dim_horizontal(msp, base_x, base_y, base_x + W, offset=-15)
    dim_vertical(msp, base_x + W, base_y, base_y + D, offset=15)

    # --- Vista frontal (front) ---
    fx = base_x + W + gap
    fy = base_y
    for name, x, z, w, h in proj_front(parts):
        rect(msp, fx + (x - ox0), fy + (z - oz0), w, h, "FRONT")
    text(msp, fx, fy + H + 10, "VISTA FRONTAL", "TEXT", 6)
    dim_horizontal(msp, fx, fy, fx + W, offset=-15)
    dim_vertical(msp, fx + W, fy, fy + H, offset=15)

    # --- Vista lateral derecha (right) ---
    rx = fx + W + gap
    ry = base_y
    for name, y, z, w, h in proj_right(parts):
        rect(msp, rx + (y - oy0), ry + (z - oz0), w, h, "RIGHT")
    text(msp, rx, ry + H + 10, "VISTA LATERAL DERECHA", "TEXT", 6)
    dim_horizontal(msp, rx, ry, rx + D, offset=-15)
    dim_vertical(msp, rx + D, ry, ry + H, offset=15)

    # --- Vista inferior (bottom) ---
    bx = base_x
    by = base_y + D + gap + H
    for name, x, y, w, h in proj_bottom(parts):
        # invertir Y para convencion de vista inferior
        rect(msp, bx + (x - ox0), by + (D - (y - oy0) - h), w, h, "BOTTOM")
    text(msp, bx, by + D + 10, "VISTA INFERIOR", "TEXT", 6)

    # --- Vista explosionada isometrica ---
    ix = rx + D + gap
    iy = base_y
    iso = proj_iso(parts, explode=max(W, D, H) * 0.35)
    for name, verts, bb, orig, newp in iso:
        # dibujar cubo isometrico (12 aristas)
        # vertices ordenados: bottom 0-1-2-3, top 4-5-6-7
        v = verts
        edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
        for a,b in edges:
            msp.add_line((ix + v[a][0], iy + v[a][1]), (ix + v[b][0], iy + v[b][1]),
                          dxfattribs={"layer": "ISO"})
        # linea de referencia (explosion) dashed
        ox_i, oy_i = iso_point(orig[0], orig[1], orig[2])
        nx_i, ny_i = iso_point(newp[0], newp[1], newp[2])
        if (ox_i, oy_i) != (nx_i, ny_i):
            msp.add_line((ix + ox_i, iy + oy_i), (ix + nx_i, iy + ny_i),
                          dxfattribs={"layer": "ISO", "linetype": "DASHED"})
        text(msp, ix + v[4][0], iy + v[4][1] + 5, name, "TEXT", 4)
    text(msp, ix, iy + (max(v[0][1] for v in [i[1] for i in iso]) if iso else 0) + 20,
         "VISTA EXPLOSIONADA", "TEXT", 6)

    path = os.path.join(outdir, f"{project}.dxf")
    doc.saveas(path)
    return path


# ---------- SVG ----------

def make_svg(parts, units, project, outdir):
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle(f"Plano: {project} (unidades: {units})", fontsize=14)

    ox0, oy0, oz0, ox1, oy1, oz1 = overall(parts)
    W = ox1 - ox0; D = oy1 - oy0; H = oz1 - oz0

    def draw_rects(ax, rects, title):
        for name, x, y, w, h in rects:
            ax.add_patch(Rectangle((x, y), w, h, fill=False, edgecolor="black", linewidth=1.2))
            ax.text(x + w/2, y + h/2, name, ha="center", va="center", fontsize=7)
        ax.set_title(title)
        ax.set_aspect("equal")
        ax.grid(True, linestyle=":", alpha=0.4)

    # Top
    r = [(n, x-ox0, y-oy0, w, h) for (n, x, y, w, h) in proj_top(parts)]
    draw_rects(axes[0, 0], r, "Vista Superior")
    axes[0, 0].set_xlim(-20, W + 20); axes[0, 0].set_ylim(-20, D + 20)

    # Front
    r = [(n, x-ox0, z-oz0, w, h) for (n, x, z, w, h) in proj_front(parts)]
    draw_rects(axes[0, 1], r, "Vista Frontal")
    axes[0, 1].set_xlim(-20, W + 20); axes[0, 1].set_ylim(-20, H + 20)

    # Right
    r = [(n, y-oy0, z-oz0, w, h) for (n, y, z, w, h) in proj_right(parts)]
    draw_rects(axes[0, 2], r, "Vista Lateral Derecha")
    axes[0, 2].set_xlim(-20, D + 20); axes[0, 2].set_ylim(-20, H + 20)

    # Bottom
    r = [(n, x-ox0, D - (y-oy0) - h, w, h) for (n, x, y, w, h) in proj_bottom(parts)]
    draw_rects(axes[1, 0], r, "Vista Inferior")
    axes[1, 0].set_xlim(-20, W + 20); axes[1, 0].set_ylim(-20, D + 20)

    # Iso / explosionada
    ax = axes[1, 1]
    iso = proj_iso(parts, explode=max(W, D, H) * 0.35)
    for name, verts, bb, orig, newp in iso:
        v = verts
        edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
        for a, b in edges:
            ax.plot([v[a][0], v[b][0]], [v[a][1], v[b][1]], "k-", linewidth=0.8)
        ox_i, oy_i = iso_point(orig[0], orig[1], orig[2])
        nx_i, ny_i = iso_point(newp[0], newp[1], newp[2])
        if (ox_i, oy_i) != (nx_i, ny_i):
            ax.plot([ox_i, nx_i], [oy_i, ny_i], "r--", linewidth=0.6)
        ax.text(v[4][0], v[4][1] + 5, name, fontsize=7)
    ax.set_title("Vista Explosionada")
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.4)

    # cotas generales
    ax2 = axes[1, 2]
    ax2.axis("off")
    ax2.text(0.05, 0.95, "COTAS GENERALES", transform=ax2.transAxes, fontsize=11, weight="bold")
    y = 0.85
    ax2.text(0.05, y, f"Largo total: {W:.0f} {units}", transform=ax2.transAxes, fontsize=9); y -= 0.08
    ax2.text(0.05, y, f"Ancho total: {D:.0f} {units}", transform=ax2.transAxes, fontsize=9); y -= 0.08
    ax2.text(0.05, y, f"Alto total:  {H:.0f} {units}", transform=ax2.transAxes, fontsize=9); y -= 0.12
    ax2.text(0.05, y, "PIEZAS:", transform=ax2.transAxes, fontsize=10, weight="bold"); y -= 0.08
    for p in parts:
        L, Wp, Hp = p["dims"]
        ax2.text(0.05, y, f"{p['name']}: {L}x{Wp}x{Hp}", transform=ax2.transAxes, fontsize=8); y -= 0.06

    plt.tight_layout()
    svg_path = os.path.join(outdir, f"{project}.svg")
    fig.savefig(svg_path, format="svg")
    pdf_path = os.path.join(outdir, f"{project}.pdf")
    fig.savefig(pdf_path, format="pdf")
    plt.close(fig)
    return svg_path, pdf_path


# ---------- PDF (reportlab) plano formal ----------

def make_pdf_reportlab(parts, units, project, outdir):
    ox0, oy0, oz0, ox1, oy1, oz1 = overall(parts)
    W = ox1 - ox0; D = oy1 - oy0; H = oz1 - oz0
    path = os.path.join(outdir, f"{project}_plano.pdf")
    c = rl_canvas.Canvas(path, pagesize=landscape(A3))
    c.setTitle(f"Plano - {project}")
    # titulo
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20 * rl_mm, 280 * rl_mm, f"PLANO DE FABRICACION: {project}")
    c.setFont("Helvetica", 10)
    c.drawString(20 * rl_mm, 272 * rl_mm, f"Unidades: {units}   |   Largo: {W:.0f}  Ancho: {D:.0f}  Alto: {H:.0f}")
    # tabla de piezas
    y = 260 * rl_mm
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20 * rl_mm, y, "PIEZAS")
    y -= 6 * rl_mm
    c.setFont("Helvetica", 9)
    for p in parts:
        L, Wp, Hp = p["dims"]
        c.drawString(20 * rl_mm, y, f"{p['name']}: {L} x {Wp} x {Hp} mm   ({p.get('material','')})")
        y -= 5 * rl_mm
    c.drawString(20 * rl_mm, y - 2 * rl_mm, "Ver archivos DXF/SVG para vistas ortogonales y explosionada.")
    c.showPage()
    c.save()
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Archivo JSON de entrada")
    ap.add_argument("--out", default="./salida", help="Directorio de salida")
    args = ap.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    project = data.get("project", "proyecto")
    units = data.get("units", "mm")
    parts = data["parts"]

    os.makedirs(args.out, exist_ok=True)

    dxf = make_dxf(parts, units, project, args.out)
    svg, pdf = make_svg(parts, units, project, args.out)
    pdf2 = make_pdf_reportlab(parts, units, project, args.out)

    print("Generado:")
    print("  DXF :", dxf)
    print("  SVG :", svg)
    print("  PDF :", pdf)
    print("  PDF (reportlab):", pdf2)


if __name__ == "__main__":
    main()
