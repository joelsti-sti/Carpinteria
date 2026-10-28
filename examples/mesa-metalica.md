# Ejemplo — Mesa metálica

## Pedido
Mesa de trabajo 1200×600×750 mm, tubo 40×40×2 mm, acero A36, carga 100 kg, profesional.

## Diseño propuesto
- Estructura de tubo cuadrado 40×40×2 mm.
- 4 patas, 4 travesaños (2 longitudinales, 2 transversales por nivel).
- Tapa de melamina 18mm sobre estructura metálica.
- Soldadura MIG + acabado pintura electrostática.

## Cálculos

**Carga por pata:**
- Carga total = 100 kg = 981 N
- Por pata = 981/4 = 245.3 N

**Verificación de pata (compresión):**
- L = 750 mm, K = 1.0
- I = 7.04 cm⁴ = 7040 mm⁴, A = 3.04 cm² = 304 mm²
- r = √(7040/304) = 4.81 mm
- λ = 750/4.81 = 155.9 → ≤ 200 ✅
- P_cr = (π² × 200000 × 7040) / 750² = 24700 N
- FS = 2.5 → P_adm = 9880 N >> 245.3 N ✅

**Deflexión de travesaño (carga distribuida):**
- w = 100/2 / 1200 = 0.0417 kg/mm = 0.409 N/mm (por travesaño)
- L = 1200 mm, E = 200000 MPa, I = 7040 mm⁴
- δ = (5 × 0.409 × 1200⁴) / (384 × 200000 × 7040) = 0.31 mm
- Límite L/360 = 3.33 mm → ✅ OK

## Lista de corte (perfiles + panel)

| Pieza | Cantidad | Largo (mm) | Material |
|---|---|---|---|
| Pata | 4 | 750 | Tubo 40×40×2 |
| Travesaño longitudinal | 2 | 1120 | Tubo 40×40×2 |
| Travesaño transversal | 2 | 520 | Tubo 40×40×2 |
| Tapa | 1 | 1200×600×18 | Melamina 18mm |

## BOM

| Item | Cantidad | Especificación |
|---|---|---|
| Tubo 40×40×2 | 8 m | Acero A36 |
| Melamina 18mm | 1 | 1200×600 |
| Tornillo M8 | 8 | Clase 8.8, 25 mm |
| Tuerca M8 | 8 | Nyloc |
| Arandela M8 | 16 | Plana |
| Electrodo E7018 | 2 kg | 3.2 mm |
| Pintura electrostática | 1 | Gris |

## Plan de corte (perfiles)

```
Barra 1 (6.0 m): 750 + 750 + 1120 + 1120 = 3740 (sobrante 2260 mm)
Barra 2 (6.0 m): 520 + 520 + 750 + 750 = 2540 (sobrante 3460 mm)
```

## Advertencias

- Verificar que el piso soporte la carga concentrada.
- Anclar a pared si se usa como mesa de trabajo con vibración.
- No exceder 100 kg de carga.
- Usar EPP en soldadura y corte.
- Verificar nivel de la mesa (ajustar patas con arandelas).
