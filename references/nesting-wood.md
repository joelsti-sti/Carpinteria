# Nesting — Madera (paneles)

## Tableros estándar por región

| Región | Dimensiones (mm) | Notas |
|---|---|---|
| Latinoamérica | 2440 × 1220 | 8×4 ft |
| Europa | 2750 × 1830 / 2070 | |
| EE.UU. | 2438 × 1219, 1524 × 1524 | 4×8 ft, 5×5 ft |
| Australia/NZ | 2400 × 1200 | |

## Kerf por tipo de máquina

| Máquina | Kerf (mm) | Notas |
|---|---|---|
| Sierra circular de mesa | 2.5–3.2 | Hoja estándar |
| Sierra de cinta | 1.5–2.0 | Corte curvo |
| CNC router | 3.0–4.0 | Fresa de 3 mm |
| Sierra de panel (beam saw) | 3.0–4.0 | Producción |

## Reglas de nesting

1. **Respetar veta:** piezas con veta marcada no se rotan 90°. Piezas sin veta (fondos, estantes interiores) pueden rotar.
2. **Márgenes:** dejar 10 mm de borde en cada lado del tablero (imperfecciones, cantos).
3. **Kerf:** aplicar kerf entre piezas adyacentes (no en bordes del tablero).
4. **Prioridad:** primero piezas grandes, luego medianas, luego pequeñas (first-fit decreasing).
5. **Grain direction:** alinear veta con el lado más largo de la pieza cuando sea posible.
6. **Sobrantes:** registrar retazos útiles (≥ 300×300 mm) para reutilización.

## Procedimiento heurístico (guillotine)

1. Ordenar piezas por área descendente.
2. Para cada pieza, buscar el rectángulo libre más pequeño que la contenga (best-fit).
3. Cortar (guillotine) y generar 2 nuevos rectángulos libres.
4. Repetir hasta colocar todas las piezas o agotar tableros.
5. Reportar piezas no colocadas y tableros adicionales necesarios.

## Formato de salida del plan de corte

Por cada tablero:
```
Tablero #1 (2440×1220 mm) — Aprovechamiento: 87%
├── Pieza A: 800×400 mm @ (0,0) [veta horizontal]
├── Pieza B: 600×300 mm @ (800,0) [veta horizontal]
├── Pieza C: 400×400 mm @ (0,400) [sin veta, rotada]
└── Sobrante: 1240×820 mm (útil)
```

## Reporte de aprovechamiento

| Métrica | Fórmula |
|---|---|
| Aprovechamiento (%) | (Σ área piezas / área tableros usados) × 100 |
| Desperdicio (%) | 100 − aprovechamiento |
| Sobrantes útiles | retazos ≥ 300×300 mm |
| Tableros necesarios | ceil(Σ área piezas / área tablero) + margen |

## Fuentes

- Dyckhoff, H. (1990) "A typology of cutting and packing problems".
- Wäscher, G. et al. (2007) "An improved typology of cutting and packing problems".
- Documentación de CutList Plus, OptiCut (formatos de exportación).
- Confianza: Media (heurísticas; validar con software dedicado para producción).
