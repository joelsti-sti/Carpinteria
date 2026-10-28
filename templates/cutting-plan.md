# Template — Plan de corte (nesting)

## Formato por tablero/perfil

```
Tablero #1 (2440×1220 mm, MDF 18mm) — Aprovechamiento: 87%
├── Pieza A: 800×400 mm @ (0,0) [veta horizontal]
├── Pieza B: 600×300 mm @ (800,0) [veta horizontal]
├── Pieza C: 400×400 mm @ (0,400) [sin veta, rotada 90°]
└── Sobrante: 1240×820 mm (útil)

Tablero #2 (2440×1220 mm, MDF 18mm) — Aprovechamiento: 72%
├── Pieza D: 1000×500 mm @ (0,0)
├── Pieza E: 500×500 mm @ (1000,0)
└── Sobrante: 1440×720 mm (útil)

Resumen:
- Tableros usados: 2
- Aprovechamiento total: 80.5%
- Desperdicio: 19.5%
- Sobrantes útiles: 2 (1240×820, 1440×720)
- Piezas no colocadas: 0
```

## Formato por perfil (1D)

```
Perfil: Tubo 40×40×2 mm (6.0 m) — 3 cortes
├── Corte 1: 1200 mm
├── Corte 2: 1800 mm
├── Corte 3: 2500 mm
└── Sobrante: 500 mm (útil)

Perfil: Tubo 40×40×2 mm (6.0 m) — 2 cortes
├── Corte 4: 2000 mm
├── Corte 5: 3800 mm
└── Sobrante: 200 mm (descarte)
```

## Reglas

- Incluir posición (x,y) de cada pieza cuando sea útil.
- Indicar si la pieza fue rotada.
- Listar sobrantes útiles (≥ 300×300 mm para paneles, ≥ 300 mm para perfiles).
- Reportar piezas que no caben en un solo tablero/perfil.
- Incluir % de aprovechamiento por tablero y total.

## Exportación

- Guardar como `plan_corte_<proyecto>.md` o `.txt`.
- Para software de nesting: exportar CSV con columnas Pieza, Largo, Ancho, Cantidad, Veta.
- Compatible con CutList Plus, OptiCut, SigmaNEST, ProNest.
