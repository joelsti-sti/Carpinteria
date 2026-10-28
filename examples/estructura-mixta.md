# Ejemplo — Estructura mixta (madera + metal)

## Pedido
Banco de trabajo 1800×700×900 mm, estructura metálica (tubo 40×40×2) + tapa de madera maciza (pino 30 mm), carga 200 kg, profesional.

## Diseño propuesto
- Estructura metálica: 4 patas, 4 travesaños longitudinales, 4 travesaños transversales, 2 refuerzos diagonales.
- Tapa de pino macizo 30 mm, atornillada a la estructura.
- Soldadura MIG + acabado pintura + barniz para madera.

## Cálculos

**Estructura metálica:**
- Carga total = 200 kg = 1962 N
- Por pata = 490.5 N
- Pata: L = 900 mm, tubo 40×40×2
  - λ = 900/4.81 = 187.1 → ≤ 200 ✅
  - P_cr = 19600 N, FS = 2.5 → P_adm = 7840 N >> 490.5 N ✅

**Tapa de madera (pino 30 mm):**
- Luz entre travesaños = 1800 − 2×40 = 1720 mm
- E = 10000 MPa (pino), I = (700×30³)/12 = 157500 mm⁴
- w = 200/1720 = 0.116 kg/mm = 1.14 N/mm
- δ = (5 × 1.14 × 1720⁴) / (384 × 10000 × 157500) = 3.8 mm
- Límite L/300 = 5.73 mm → ✅ OK (3.8 < 5.73)

**Unión madera-metal (tornillos):**
- 8 tornillos M8 clase 8.8, atornillados a la estructura.
- Carga por tornillo = 200/8 = 25 kg = 245 N
- Resistencia de perno M8 clase 8.8: Rn = 0.75 × 800 × 50.3 = 30180 N >> 245 N ✅

## Lista de corte

### Metal

| Pieza | Cantidad | Largo (mm) | Perfil |
|---|---|---|---|
| Pata | 4 | 900 | Tubo 40×40×2 |
| Travesaño longitudinal | 4 | 1720 | Tubo 40×40×2 |
| Travesaño transversal | 4 | 620 | Tubo 40×40×2 |
| Refuerzo diagonal | 2 | 950 | Tubo 40×40×2 |

### Madera

| Pieza | Cantidad | Largo×Ancho×Espesor (mm) | Material |
|---|---|---|---|
| Tapa | 1 | 1800×700×30 | Pino macizo |

## BOM

| Item | Cantidad | Especificación |
|---|---|---|
| Tubo 40×40×2 | 12 m | Acero A36 |
| Pino 30 mm | 1 | 1800×700 |
| Tornillo M8 | 8 | Clase 8.8, 40 mm |
| Tuerca M8 | 8 | Nyloc |
| Arandela M8 | 16 | Plana |
| Electrodo E7018 | 3 kg | 3.2 mm |
| Pintura electrostática | 1 | Negro mate |
| Barniz poliuretano | 1 | Para madera |

## Plan de corte

### Metal

```
Barra 1 (6.0 m): 900 + 900 + 1720 + 1720 = 5240 (sobrante 760 mm)
Barra 2 (6.0 m): 620×4 + 950×2 = 2480 + 1900 = 4380 (sobrante 1620 mm)
```

### Madera

Un tablero de pino macizo 1800×700×30 mm (o unir 2 piezas).

## Instrucciones de ensamble

1. Cortar perfiles metálicos y madera.
2. Armar estructura metálica (tacking + soldadura completa).
3. Lijar y pintar estructura.
4. Preparar tapa de madera (lijar, barnizar).
5. Atornillar tapa a estructura (8 tornillos M8).
6. Verificar nivel y estabilidad.

## Advertencias

- Verificar que el piso soporte la carga concentrada (200 kg).
- Anclar a pared si se usa en taller con vibración.
- No exceder 200 kg de carga.
- Usar EPP en soldadura y corte.
- Verificar que la tapa de madera esté bien fijada (sin movimiento).
- Acimatar madera antes de barnizar (evitar deformaciones).
