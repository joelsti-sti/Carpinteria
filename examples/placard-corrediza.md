# Ejemplo — Placard corredizo

## Pedido
Placard de 2000×1800×600 mm, melamina 18mm, 2 puertas corredizas, DIY.

## Diseño propuesto
- Estructura: 2 laterales, techo, base, fondo, divisor central.
- 2 puertas corredizas (900×1800×18) en guías de aluminio.
- Interior: 2 estantes regulables + 1 barra colgante.

## Cálculos

**Guías corredizas:**
- Peso por puerta: 900×1800×18 mm melamina = 0.9×1.8×0.018×700 = 20.4 kg
- Carga total sobre guía: 20.4 kg → usar guía de aluminio para 40 kg (margen 2×).
- Holgura lateral: 13 mm por lado → ancho puerta = (2000 − 2×13)/2 = 987 mm (usar 980 mm).

**Estantes interiores:**
- Luz = 900 mm (entre divisor y lateral), melamina 18mm
- δ_max = 900/300 = 3 mm, carga 15 kg/m
- w = 15/1000 = 0.015 kg/mm = 0.147 N/mm
- I = (600×18³)/12 = 29160 mm⁴, E = 2200 MPa
- δ = (5×0.147×900⁴)/(384×2200×29160) = 0.32 mm → ✅ OK

## Lista de corte (resumen)

| Pieza | Cantidad | Largo×Ancho×Espesor (mm) |
|---|---|---|
| Lateral | 2 | 1800×600×18 |
| Techo/Base | 2 | 2000×600×18 |
| Divisor | 1 | 1800×600×18 |
| Fondo | 1 | 1964×1764×6 (MDF) |
| Estante | 2 | 900×580×18 |
| Puerta | 2 | 1800×980×18 |

## BOM

| Item | Cantidad | Especificación |
|---|---|---|
| Guía corrediza aluminio | 2 pares | 2000 mm, 40 kg |
| Tornillo aglomerado | 40 | 4×50 mm |
| Barra colgante | 1 | 900 mm + soportes |
| Bisagra (si aplica) | — | — |
| Canto PVC | 15 m | 22 mm |

## Plan de corte

2 tableros de melamina 2440×1220 mm. Aprovechamiento ~78%.

## Advertencias

- Verificar que el piso esté nivelado.
- Fijar a pared (anti-vuelco).
- Puertas corredizas requieren guías de calidad para evitar descarrilamiento.
- Peso total del placard > 100 kg → verificar capacidad del piso.
