# Ejemplo — Estante de madera

## Pedido
Estante de pared, 1000×250×200 mm, melamina 18mm, carga 20 kg distribuida, DIY.

## Diseño propuesto
- 1 estante (1000×250×18)
- 2 soportes laterales (200×250×18)
- 1 travesaño trasero (964×50×18) — refuerzo
- Fijación a pared con 4 escuadras metálicas

## Cálculos

**Flecha del estante:**
- L = 1000 mm, w = 20 kg / 1000 mm = 0.02 kg/mm = 0.196 N/mm
- E = 2200 MPa (melamina), I = (250 × 18³)/12 = 12150 mm⁴
- δ = (5 × 0.196 × 1000⁴) / (384 × 2200 × 12150) = 0.96 mm
- Límite L/300 = 3.33 mm → ✅ OK (0.96 < 3.33)

**Carga máxima:**
- w_max = (3.33 × 384 × 2200 × 12150) / (5 × 1000⁴) = 0.67 N/mm
- W_total = 0.67 × 1000 = 670 N ≈ 68 kg → margen de seguridad 3.4×

## Lista de corte

| Pieza | Cantidad | Largo×Ancho×Espesor (mm) | Material | Canto |
|---|---|---|---|---|
| Estante | 1 | 1000×250×18 | Melamina | Frontal |
| Soporte lateral | 2 | 200×250×18 | Melamina | Frontal |
| Travesaño | 1 | 964×50×18 | Melamina | — |

## BOM

| Item | Cantidad | Especificación |
|---|---|---|
| Escuadra metálica | 4 | 25×25×2 mm |
| Tornillo aglomerado | 8 | 4×40 mm |
| Tornillo pared | 4 | 6×60 mm + tarugo |
| Canto PVC | 1.5 m | 22 mm |

## Plan de corte

Un tablero de melamina 2440×1220 mm suficiente. Aprovechamiento ~65%.

## Instrucciones de ensamble

1. Cortar piezas según lista.
2. Aplicar canto frontal al estante.
3. Atornillar soportes laterales a la pared con escuadras.
4. Atornillar travesaño trasero entre soportes.
5. Colocar estante sobre soportes y fijar con tornillos.
6. Verificar nivel y escuadra.

## Advertencias

- Fijar a pared obligatorio (anti-vuelco).
- No exceder 20 kg de carga.
- Verificar que la pared soporte la carga.
