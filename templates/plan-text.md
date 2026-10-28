# Template — Plano textual (para PDF)

## Estructura del plano

```
========================================
PLANO DE FABRICACIÓN: <Nombre del mueble>
Proyecto: <nombre>  |  Fecha: <fecha>  |  Unidades: mm
========================================

1. VISTA FRONTAL
   ┌─────────────────────┐
   │                     │  Alto: XXX mm
   │                     │  Ancho: XXX mm
   │                     │
   └─────────────────────┘

2. VISTA LATERAL
   ┌────┐
   │    │  Profundidad: XXX mm
   │    │
   └────┘

3. CORTES Y DIMENSIONES
   - Pieza A: XXX × XXX × XX mm (cantidad: X)
   - Pieza B: XXX × XXX × XX mm (cantidad: X)

4. HERRAJES
   - Bisagras: X unidades, posición a XX mm del borde
   - Tornillos: X unidades, Ø X mm, largo XX mm

5. NOTAS DE FABRICACIÓN
   - Material: XXX
   - Acabado: XXX
   - Tolerancia: ±0.5 mm
   - Canto: especificar bordes

6. SEGURIDAD
   - Carga máxima por estante: XX kg
   - Fijar a pared: Sí/No
   - Anti-vuelco: Sí/No
========================================
```

## Reglas

- Incluir vistas (frontal, lateral, superior) en ASCII o descripción.
- Listar todas las piezas con dimensiones y cantidad.
- Especificar herrajes con posiciones.
- Incluir notas de fabricación (material, acabado, tolerancia, canto).
- Incluir sección de seguridad (cargas, fijación).
- Para PDF: convertir a formato imprimible (A4/A3) con márgenes.
- Para metal: incluir detalles de soldadura (tamaño de cordón, longitud).

## Exportación

- Guardar como `plano_<proyecto>.md` o `.pdf`.
- Para PDF: usar pandoc, wkhtmltopdf, o exportar desde Markdown.
- Para CAD: exportar como DXF (requiere software externo).
- Compatible con impresión en A4 (márgenes 10 mm).
