# Nesting — Metal (chapas y perfiles)

## Chapas estándar

| Región | Dimensiones (mm) | Notas |
|---|---|---|
| Latinoamérica | 2440 × 1220 | 8×4 ft |
| Europa | 3000 × 1500 / 2500 × 1250 | |
| EE.UU. | 2438 × 1219 | 4×8 ft |
| Coil | 1220 (ancho) × largo variable | Requiere corte previo |

## Kerf por proceso de corte

| Proceso | Kerf (mm) | Notas |
|---|---|---|
| Plasma (aire) | 1.5–3.0 | Depende de amperaje |
| Plasma (oxígeno) | 1.0–2.0 | Acero carbono |
| Láser (CO₂/fibra) | 0.1–0.5 | Alta precisión |
| Oxicorte | 3.0–6.0 | Solo acero carbono |
| Sierra de cinta | 1.5–2.0 | Perfiles |
| Sierra circular (metal) | 2.0–3.0 | Tubos y barras |
| Punzonado (punching) | 0 (sin kerf) | Con herramienta dedicada |

## Reglas de nesting para chapas

1. **Veta (grain):** en chapas laminadas en frío, la veta afecta el doblado. No rotar piezas que se van a doblar.
2. **Márgenes:** 5–10 mm de borde (imperfecciones, mordazas).
3. **Kerf:** aplicar entre piezas adyacentes.
4. **Doblado:** dejar margen de doblado (bend allowance) según espesor y radio.
5. **Sobrantes:** registrar retazos ≥ 200×200 mm.
6. **Dirección de laminado:** orientar piezas estructurales con la veta para mejor resistencia.

## Corte lineal de perfiles (1D)

### Perfiles estándar (barras)

| Perfil | Largo estándar (m) | Notas |
|---|---|---|
| Tubo cuadrado/rectangular | 6.0 | Algunos 3.0 |
| Ángulo | 6.0 | |
| Canal U | 6.0 | |
| Viga I/H | 6.0–12.0 | |
| Solera | 6.0 | |
| Varilla | 3.0–6.0 | |

### Kerf por máquina (perfiles)

| Máquina | Kerf (mm) |
|---|---|
| Sierra de cinta | 1.5–2.0 |
| Sierra circular | 2.0–3.0 |
| Plasma manual | 2.0–3.0 |
| Corte por abrasión | 3.0–4.0 |

## Procedimiento de optimización 1D (perfiles)

1. Ordenar cortes por longitud descendente.
2. First-fit decreasing: colocar cada corte en la barra con menos espacio libre que lo contenga.
3. Si no cabe en ninguna barra existente, abrir nueva barra.
4. Reportar barras usadas, desperdicio y sobrantes.

## Formato de salida del plan de corte (metal)

```
Chapa #1 (2440×1220 mm, 1.5 mm) — Aprovechamiento: 82%
├── Pieza A: 800×500 mm @ (0,0) [veta horizontal, sin doblar]
├── Pieza B: 600×400 mm @ (800,0)
├── Pieza C: 400×300 mm @ (0,500)
└── Sobrante: 1240×720 mm (útil)

Perfil: Tubo 40×40×2 mm (6.0 m) — 3 cortes
├── Corte 1: 1200 mm
├── Corte 2: 1800 mm
├── Corte 3: 2500 mm
└── Sobrante: 500 mm (útil)
```

## Fuentes

- Dyckhoff, H. (1990) "A typology of cutting and packing problems".
- Documentación de SigmaNEST, ProNest (formatos de exportación).
- AWS D1.1 (márgenes de soldadura y corte).
- Confianza: Media (heurísticas; validar con software dedicado para producción).
