# Herrajes — Metal

## Pernos y tornillos metálicos

| Clase | fy (MPa) | fu (MPa) | Uso típico |
|---|---|---|---|
| 4.6 | 240 | 400 | No estructural, cargas bajas |
| 5.8 | 400 | 500 | Uso general |
| 8.8 | 640 | 800 | Estructural (recomendado) |
| 10.9 | 900 | 1000 | Alta resistencia |
| 12.9 | 1080 | 1200 | Cargas extremas |

**Diámetros comunes:** M6, M8, M10, M12, M16, M20.

**Resistencia a tracción de perno (AISC):**
```
Rn = 0.75 × fu × Ab
```
Donde Ab = área de la sección (mm²). Aplicar factor de seguridad φ = 0.75.

**Resistencia a cortante (doble cortante):** Rn = 2 × (0.6 × fu × Ab) con φ = 0.75.

## Tuercas

| Tipo | Uso |
|---|---|
| Hexagonal estándar | General |
| Nyloc (autoblocante) | Vibración, cargas dinámicas |
| Castilla (castle nut) | Ejes, pasadores |
| Tuerca de seguridad (prevailing torque) | Desmontaje frecuente |

## Arandelas

| Tipo | Uso |
|---|---|
| Plana (SAE) | Distribución de carga |
| Crenada (lock washer) | Anti-loosening (limitado) |
| Grower (ondulada) | Vibración leve |

## Remaches

| Tipo | Diámetro (mm) | Carga (kg/remache) | Uso |
|---|---|---|---|
| Pop (blind) | 3, 4, 5, 6 | 50–200 | Chapa delgada, acceso unilateral |
| Estructural (grooved) | 4, 5, 6 | 200–500 | Cargas medias |
| Sólido (rivet) | 4–10 | 300–1000 | Alta resistencia, acceso bilateral |

## Tornillos autoperforantes para metal

| Tipo | Punta | Uso |
|---|---|---|
| Punta broca (#2, #3) | Autotaladrante | Chapa 0.5–3 mm |
| Punta aguda (self-drilling) | Autoperforante | Chapa delgada |
| Tornillo TEK | Broca + rosca | Estructuras ligeras |

## Soldadura

### Tipos de electrodo (SMAW/arco)

| Electrodo | Uso | Posición |
|---|---|---|
| E6010 | Raíz, penetración profunda | Todas |
| E6013 | Propósito general, acabado suave | Todas |
| E7018 | Alta resistencia, baja hidrógeno | Todas |
| E308L | Inoxidable | Todas |

### Procesos MIG/MAG

| Gas | Material | Notas |
|---|---|---|
| Ar/CO₂ (75/25) | Acero carbono | Uso general |
| CO₂ puro | Acero carbono | Económico, más salpicadura |
| Ar puro | Aluminio | Requiere antorcha spool gun |
| Ar/He | Aluminio grueso | Mejor penetración |

### Tamaño de cordón

```
t_min = espesor del material más delgado (máx. 8 mm por pasada)
Longitud efectiva = longitud total − 2 × (2 × t)  [cráteres]
```

**Resistencia de cordón (AISC):**
```
Rn = 0.75 × 0.6 × fu_electrodo × 0.707 × t × L
```
Donde t = tamaño del cordón (mm), L = longitud efectiva (mm). φ = 0.75.

### TIG

- Acero inox: tungsteno 2% torio o cerio, gas Ar.
- Aluminio: tungsteno puro o circonio, AC, gas Ar.
- Acero carbono: tungsteno 2% torio, gas Ar/He.

## Bisagras y herrajes metálicos

| Tipo | Uso | Carga (kg) |
|---|---|---|
| Bisagra de piano (metal) | Tapas, puertas largas | 15–30 por metro |
| Bisagra de codo soldada | Puertas de gabinete | 5–10 |
| Bisagra de resorte | Puertas de vaivén | 3–8 |
| Bisagra de ajuste 3D | Puertas de mueble (aluminio) | 5–15 |

## Fuentes

- AISC Steel Construction Manual.
- AWS D1.1 (soldadura estructural).
- ISO 898-1 (pernos clase 8.8/10.9).
- Catálogos: Ternium, Siderar, Alcoa, Hafele.
- Confianza: Alta para propiedades; Media para valores de diseño (verificar normativa local).
