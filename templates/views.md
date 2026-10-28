# Template — Vistas y cotas (CAD/PDF)

## Vistas ortogonales generadas

El script `scripts/generate_plans.py` genera automáticamente:

1. **Vista Superior (Top)** — proyección X-Y, con cotas de largo y ancho.
2. **Vista Frontal (Front)** — proyección X-Z, con cotas de largo y alto.
3. **Vista Lateral Derecha (Right)** — proyección Y-Z, con cotas de ancho y alto.
4. **Vista Inferior (Bottom)** — proyección X-Y invertida.
5. **Vista Explosionada (Isométrica)** — piezas separadas con líneas de referencia.

## Cotas

- Cotas generales (overall): largo, ancho, alto.
- Cotas por pieza: dimensiones (L×A×H).
- Cotas en DXF: líneas de extensión + línea de cota + texto.
- Cotas en SVG/PDF: anotaciones en panel lateral.

## Uso

```bash
cd ~/.config/opencode/skills/muebles-a-medida/scripts
python generate_plans.py input.json --out ./salida
```

Entrada: archivo JSON con proyecto, unidades y lista de piezas (nombre, dims [L,A,H], pos [x,y,z], material).

Salida:
- `<proyecto>.dxf` — vistas ortogonales + explosionada, capas por vista.
- `<proyecto>.svg` — vistas en formato vectorial.
- `<proyecto>.pdf` — vistas para impresión.
- `<proyecto>_plano.pdf` — plano formal con tabla de piezas.

## Formato de entrada (JSON)

```json
{
  "project": "nombre-proyecto",
  "units": "mm",
  "parts": [
    {"name": "Pieza", "dims": [1000, 250, 18], "pos": [0, 0, 0], "material": "Melamina 18mm"}
  ]
}
```

- `dims`: [Largo, Ancho, Alto] en las unidades elegidas.
- `pos`: [x, y, z] posición de la esquina inferior-izquierda-posterior.
- Las piezas se proyectan automáticamente en todas las vistas.

## Convenciones de vistas

- Vista superior: X (largo) horizontal, Y (ancho) vertical.
- Vista frontal: X (largo) horizontal, Z (alto) vertical.
- Vista lateral derecha: Y (ancho) horizontal, Z (alto) vertical.
- Vista inferior: igual a superior, invertida en Y.
- Explosionada: isométrica con separación radial desde el centroide.

## Exportación a CAD

- DXF generado es compatible con AutoCAD, LibreCAD, DraftSight, etc.
- Abrir en LibreCAD (gratuito) para editar cotas y exportar a PDF/DWG.
- Para convertir DXF a PDF: usar LibreCAD o `dxf2pdf` (si está instalado).

## Notas

- Las vistas son proyecciones de cajas (bounding boxes). Para geometría compleja, editar el DXF manualmente.
- La vista explosionada usa separación radial automática; ajustar el factor de explosión en el script si es necesario.
- Cotas generales se calculan a partir del bounding box total.
