# Ejemplo — Rack metálico

## Pedido
Rack para TV de 1500×400×500 mm, tubo 25×25×1.5 mm, acero A36, carga 50 kg, DIY.

## Diseño propuesto
- Estructura de tubo cuadrado 25×25×1.5 mm.
- 4 patas, 2 travesaños longitudinales, 2 travesaños transversales por nivel.
- 2 niveles (TV arriba, equipos abajo).
- Soldadura MIG (Ar/CO₂ 75/25).

## Cálculos

**Carga por pata:**
- Carga total = 50 kg = 490.5 N
- Por pata = 490.5/4 = 122.6 N

**Verificación de pata (compresión):**
- L = 500 mm, K = 1.0 (articulada-articulada)
- I = 1.22 cm⁴ = 1220 mm⁴, A = 1.35 cm² = 135 mm²
- r = √(I/A) = √(1220/135) = 3.0 mm
- λ = (1.0×500)/3.0 = 166.7 → ≤ 200 ✅
- P_cr = (π² × 200000 × 1220) / (1×500)² = 9630 N
- FS = 4 → P_adm = 9630/4 = 2407 N >> 122.6 N ✅

**Soldadura:**
- Espesor = 1.5 mm → t_min = 3 mm (AWS D1.1)
- Cordón de 3 mm, longitud efectiva = L − 2×(2×3) = L − 12

## Lista de corte (perfiles)

| Pieza | Cantidad | Largo (mm) | Perfil |
|---|---|---|---|
| Pata | 4 | 500 | Tubo 25×25×1.5 |
| Travesaño longitudinal | 4 | 1460 | Tubo 25×25×1.5 |
| Travesaño transversal | 4 | 360 | Tubo 25×25×1.5 |

## BOM

| Item | Cantidad | Especificación |
|---|---|---|
| Tubo 25×25×1.5 | 6 m | Acero A36 |
| Electrodo E7018 | 1 kg | 2.5 mm |
| Gas Ar/CO₂ | 1 | Balón pequeño |
| Disco de corte | 2 | 115 mm |
| Pintura electrostática | 1 | Negro mate |

## Plan de corte (perfiles)

Barra de 6.0 m → 3 cortes de 500 mm (sobrante 4500 mm) — mejor optimizar:

```
Barra 1 (6.0 m): 1460 + 1460 + 1460 + 1460 = 5840 (sobrante 160 mm)
Barra 2 (6.0 m): 500×4 + 360×4 = 2000 + 1440 = 3440 (sobrante 2560 mm)
```

## Instrucciones de ensamble (soldadura)

1. Cortar perfiles según lista.
2. Preparar juntas (limpiar, biselar si espesor > 3 mm).
3. Armar estructura en posición (usar escuadra magnética).
4. Soldar puntos de tacking en cada unión.
5. Soldar cordones completos (3 mm, MIG, 18–20V, 120–140A).
6. Inspeccionar cordones (visual, sin poros ni grietas).
7. Lijar y pintar.

## Advertencias

- Verificar nivel de las patas (ajustar con arandelas si es necesario).
- Anclar a pared si la relación alto/ancho > 3:1.
- No exceder 50 kg de carga.
- Usar EPP: careta, guantes, delantal de cuero.
- Ventilar el área de soldadura.
