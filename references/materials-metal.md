# Materiales — Metal

## Tabla de propiedades mecánicas

| Material | Densidad (kg/m³) | E (GPa) | fy (MPa) | fu (MPa) | Confianza |
|---|---|---|---|---|---|
| Acero A36 (carbono) | 7850 | 200 | 250 | 400 | Alta |
| Acero S235 (Europa) | 7850 | 210 | 235 | 360 | Alta |
| Acero S355 | 7850 | 210 | 355 | 510 | Alta |
| Acero inox 304 | 8000 | 193 | 205 | 515 | Alta |
| Acero inox 316 | 8000 | 193 | 205 | 515 | Alta |
| Acero galvanizado (Z275) | 7850 | 200 | 250–350 | 400–500 | Media |
| Aluminio 6061-T6 | 2700 | 69 | 276 | 310 | Alta |
| Aluminio 6063-T5 | 2700 | 69 | 145 | 186 | Alta |
| Aluminio 5052-H32 | 2680 | 70 | 193 | 228 | Alta |

fy = límite elástico; fu = resistencia última; E = módulo de Young.

## Perfiles estructurales estándar

### Tubo cuadrado/rectangular (mm)

| Perfil | Área (cm²) | I (cm⁴) | Módulo sección (cm³) | Peso (kg/m) |
|---|---|---|---|---|
| 20×20×1.5 | 1.05 | 0.59 | 0.59 | 0.83 |
| 25×25×1.5 | 1.35 | 1.22 | 0.98 | 1.06 |
| 30×30×2 | 2.24 | 2.88 | 1.92 | 1.76 |
| 40×40×2 | 3.04 | 7.04 | 3.52 | 2.39 |
| 40×40×3 | 4.44 | 9.68 | 4.84 | 3.49 |
| 50×50×2 | 3.84 | 14.4 | 5.76 | 3.01 |
| 50×50×3 | 5.64 | 20.1 | 8.04 | 4.43 |
| 60×60×3 | 6.84 | 35.6 | 11.9 | 5.37 |
| 80×80×3 | 9.24 | 87.4 | 21.9 | 7.25 |

### Ángulo (mm)

| Perfil | Área (cm²) | I (cm⁴) | Peso (kg/m) |
|---|---|---|---|
| 25×25×3 | 1.41 | 0.98 | 1.11 |
| 30×30×3 | 1.71 | 1.71 | 1.34 |
| 40×40×4 | 3.04 | 4.46 | 2.39 |
| 50×50×5 | 4.75 | 10.8 | 3.73 |
| 60×60×6 | 6.84 | 23.0 | 5.37 |

### Canal U y viga I (consultar tablas de fabricante)

Valores dependen de la norma (UPN, IPN, IPE, HEA, HEB). Usar tablas del fabricante (ArcelorMittal, Ternium).

## Chapas / láminas

| Calibre (ga) | Espesor (mm) | Peso (kg/m²) |
|---|---|---|
| 14 ga | 1.90 | 15.0 |
| 16 ga | 1.50 | 11.8 |
| 18 ga | 1.20 | 9.4 |
| 20 ga | 0.90 | 7.1 |
| 22 ga | 0.75 | 5.9 |

## Reglas de diseño para metal

- **Pandeo:** verificar esbeltez (λ = L/r) en columnas y puntales. Límite típico λ ≤ 200 (compresión) / λ ≤ 300 (tracción).
- **Soldadura:** tamaño mínimo de cordón = espesor del material más delgado (máx. 8 mm para una pasada).
- **Pernos:** clase 8.8 (fy=640 MPa) para estructural; 10.9 para alta resistencia.
- **Deflexión de viga:** límite típico L/360 para carga viva, L/240 para carga muerta.
- **Conexiones:** siempre verificar el elemento más débil (base metal, cordón, perno).

## Fuentes

- AISC Steel Construction Manual (15th/16th ed.).
- Eurocódigo 3 (EN 1993).
- AWS D1.1 (soldadura estructural acero).
- Tablas de perfiles: Ternium, ArcelorMittal, Alcoa.
- Shigley — Mechanical Engineering Design (pernos, uniones).
- Confianza: Alta para propiedades mecánicas; Media para valores de diseño (verificar con normativa local).
