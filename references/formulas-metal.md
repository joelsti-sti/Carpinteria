# Fórmulas — Metal

## Flexión de viga (acero/aluminio)

**Viga simplemente apoyada, carga distribuida:**
```
δ = (5 × w × L⁴) / (384 × E × I)
M_max = (w × L²) / 8
σ = M / S  (S = módulo de sección)
```
- Verificar σ ≤ fy / FS (factor de seguridad).
- Límite de flecha: δ ≤ L/360 (carga viva), L/240 (carga muerta).

**Viga en voladizo:**
```
δ = (w × L⁴) / (8 × E × I)
M_max = (w × L²) / 2
```

## Pandeo (Euler)

**Columna articulada-articulada:**
```
P_cr = (π² × E × I) / (K × L)²
```
- K = factor de longitud efectiva (1.0 articulada-articulada, 0.5 empotrada-empotrada, 0.7 empotrada-articulada, 2.0 voladizo).
- Verificar P_aplicada ≤ P_cr / FS (FS ≥ 2 para compresión).

**Esbeltez:**
```
λ = (K × L) / r   (r = radio de giro = √(I/A))
```
- Límite: λ ≤ 200 (compresión), λ ≤ 300 (tracción).

## Tracción

```
Rn = 0.75 × fu × An   (área neta)
```
- φ = 0.75 (LRFD) o FS = 2 (ASD).

## Cortante

```
Rn = 0.6 × fy × Aw   (Aw = área del alma)
```

## Soldadura — resistencia de cordón

```
Rn = 0.75 × 0.6 × fu_electrodo × 0.707 × t × L_eff
```
- t = tamaño del cordón (mm)
- L_eff = longitud efectiva = L_total − 2 × (2t) [cráteres]
- φ = 0.75

**Tamaño mínimo de cordón (AWS D1.1):**
- Material ≤ 6 mm: t_min = 3 mm
- 6–13 mm: t_min = 5 mm
- > 13 mm: t_min = 6 mm (o espesor del material más delgado si < 6)

## Pernos — resistencia

**Tracción:**
```
Rn = 0.75 × fu × Ab
```
**Cortante (doble cortante):**
```
Rn = 2 × (0.6 × fu × Ab) × φ (φ = 0.75)
```
**Combinada (interacción):**
```
(f_r/F_r) + (f_t/F_t) ≤ 1.0
```

## Conexiones atornilladas — arrancamiento

```
Rn = 1.2 × Lc × t × fu
```
- Lc = distancia libre (mm)
- t = espesor (mm)
- fu = resistencia última del material base (MPa)

## Deflexión de viga con carga puntual

```
δ = (P × L³) / (48 × E × I)
```

## Estabilidad de estructura (rack)

```
Momento vuelco = W_carga × brazo
Momento estabilizador = W_estructura × (base/2) + anclaje
Condición: M_est ≥ 1.5 × M_vuelco
```

## Fuentes

- AISC Steel Construction Manual.
- Eurocódigo 3 (EN 1993).
- AWS D1.1.
- Shigley — Mechanical Engineering Design.
- Confianza: Alta para fórmulas; Media para valores de diseño.
