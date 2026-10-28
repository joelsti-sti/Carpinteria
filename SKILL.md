---
name: muebles-a-medida
description: Diseño, cálculo y optimización de muebles y estructuras a medida en madera y metal. Cubre estantes, placares, cajoneras, racks, marcos, puertas corredizas y abatibles, cálculo de neumáticos/gas lifts, selección de herrajes (bisagras, correderas, guías, tornillos, clavos, pernos, soldadura), listas de corte, BOM, nesting de paneles/perfiles, y generación de planos textuales y archivos CSV/PDF. Soporta unidades métricas y pulgadas, normativa por región (AISC, Eurocódigo, NTC/NOM, etc.) y públicos profesional/DIY.
metadata:
  version: "1.0"
---

# Muebles a Medida — Carpintería de Madera y Metal

Skill para diseñar, calcular y optimizar muebles y estructuras a medida en **madera y metal**, con generación de entregables (listas de corte, BOM, planos, instrucciones de ensamble).

## Cuándo usar esta skill

Activa esta skill cuando el usuario pida:
- Diseñar un mueble o estructura a medida (estante, placard, cajonera, rack, marco, mesa, gabinete, puerta).
- Calcular cargas, flechas, fuerzas, cantidades de herrajes/tornillos/clavos.
- Seleccionar neumáticos/gas lifts para puertas abatibles.
- Optimizar corte de tableros, chapas o perfiles (nesting).
- Generar lista de corte, BOM, plano textual o instrucciones de ensamble.
- Convertir entre unidades métricas y pulgadas.

## Alcance

**Materiales:**
- Madera y derivados: MDF, melamina, MDP, contrachapado, OSB, madera maciza (pino, roble, etc.).
- Metal: acero carbono/inox/galvanizado, aluminio, perfiles (tubo, ángulo, canal, viga I/H, solera, varilla), chapas.

**Uniones:**
- Madera: atornillado, clavado, encolado, ensambles.
- Metal: soldadura (MIG/MAG, TIG, SMAW), atornillado, remachado, pernos pretensados.

**Estructuras:** estantes, placares, cajoneras, racks, marcos, mesas, gabinetes, puertas corredizas/abatibles, soportes.

**Normativa por región selectable:** AISC (EE.UU.), Eurocódigo (Europa), NTC/NOM (Latinoamérica), AS/NZS (Australia/NZ), o modo "genérico/conservador".

## Flujo de trabajo recomendado

1. **Recolectar datos** del usuario (dimensiones, material, carga, región, unidades, tipo de máquina de corte).
2. **Proponer diseño** (distribución, espesores, refuerzos).
3. **Calcular** (flechas, cargas, fuerzas, cantidades).
4. **Optimizar corte** (nesting de paneles/perfiles).
5. **Generar entregables** (lista de corte, BOM, plano, instrucciones).
6. **Validar seguridad** (checklist + advertencias).

Si faltan datos, aplicar **defaults razonables** (ver `references/`) y declararlos explícitamente.

## Defaults razonables

| Parámetro | Default |
|---|---|
| Espesor panel madera | 18 mm (melamina/MDF) |
| Espesor chapa metal | 1.5 mm (calibre ~16 ga) |
| Factor de seguridad madera | 3 (DIY) / 2 (profesional) |
| Factor de seguridad metal | 4 (DIY) / 2.5 (profesional) |
| Kerf sierra circular madera | 3 mm |
| Kerf plasma metal | 2 mm |
| Unidades | métricas (mm) |
| Región/normativa | genérico/conservador |
| Carga de estante residencial | 15 kg/m (distribuida) |

## Formato de salida estándar

Toda respuesta debe incluir (cuando aplique):

1. **Resumen del diseño** (qué se construye, dimensiones, material).
2. **Cálculos** (fórmulas + valores + unidades).
3. **Lista de corte** (pieza, cantidad, largo×ancho×espesor, canto) — con opción CSV.
4. **BOM de herrajes/consumibles** (ítem, cantidad, especificación) — con opción CSV.
5. **Plan de corte optimizado** (nesting por tablero/perfil).
6. **Instrucciones de ensamble** (pasos numerados).
7. **Advertencias y límites** (seguridad, cargas máximas).
8. **Estimación de costo** (opcional, placeholder si no hay precios).

## Optimización de materiales (nesting)

- **Paneles 2D:** distribuir piezas en tableros estándar o stock propio, respetando veta, kerf y márgenes.
- **Perfiles 1D:** optimizar corte de barras/tubos.
- **Reporte:** % aprovechamiento, sobrantes útiles, desperdicio, número de tableros/barras.
- **Diagrama de corte:** descripción por tablero (pieza + posición) o ASCII.

Ver `references/nesting-wood.md` y `references/nesting-metal.md`.

## Unidades

Soporta mm, cm, m, in, ft. Conversión automática. Ver `references/units.md`.

## Seguridad

Checklist obligatorio en cada diseño (anti-vuelco, topes, carga por nivel, fijación a pared/piso, soldadura mínima). Ver `references/safety.md`.

## Fuentes y referencias

Todas las tablas incluyen cita de fuente, edición/año y nivel de confianza. Ver `references/sources.md`.

## Generación de planos CAD/PDF

La skill incluye un generador de planos en `scripts/generate_plans.py` que produce:
- **DXF**: vistas ortogonales (superior, frontal, lateral, inferior) + vista explosionada isométrica, con cotas.
- **SVG**: vistas en formato vectorial.
- **PDF**: vistas para impresión + plano formal con tabla de piezas.

Uso:
```bash
cd scripts
python generate_plans.py input.json --out ./salida
```

Ver `templates/views.md` para formato de entrada y convenciones.

## Referencias

- [Materiales — Madera](references/materials-wood.md)
- [Materiales — Metal](references/materials-metal.md)
- [Herrajes — Madera](references/hardware-wood.md)
- [Herrajes — Metal](references/hardware-metal.md)
- [Fórmulas — Madera](references/formulas-wood.md)
- [Fórmulas — Metal](references/formulas-metal.md)
- [Nesting — Madera](references/nesting-wood.md)
- [Nesting — Metal](references/nesting-metal.md)
- [Unidades](references/units.md)
- [Seguridad](references/safety.md)
- [Fuentes](references/sources.md)

## Templates

- [Vistas y cotas (CAD/PDF)](templates/views.md)
- [Lista de corte CSV](templates/cutlist.csv.md)
- [BOM CSV](templates/bom.csv.md)
- [Plan de corte](templates/cutting-plan.md)
- [Ensamble](templates/assembly.md)
- [Plano textual](templates/plan-text.md)

## Ejemplos

- [Estante de madera](examples/estante-madera.md)
- [Placard corredizo](examples/placard-corrediza.md)
- [Rack metálico](examples/rack-metal.md)
- [Mesa metálica](examples/mesa-metalica.md)
- [Estructura mixta](examples/estructura-mixta.md)
