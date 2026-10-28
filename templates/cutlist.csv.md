# Template — Lista de corte (CSV)

## Formato CSV

```csv
Pieza,Cantidad,Largo (mm),Ancho (mm),Espesor (mm),Material,Canto,Notas
Estante,2,800,300,18,Melamina 18mm,Frontal+trasero,Interior
Lateral,2,1800,300,18,Melamina 18mm,Frontal+trasero,Exterior
Fondo,1,764,1764,6,MDF 6mm,Todos,Trasero
Tapa,1,836,336,18,Melamina 18mm,Todos,Superior
```

## Columnas

| Columna | Descripción |
|---|---|
| Pieza | Nombre de la pieza |
| Cantidad | Número de unidades |
| Largo | Dimensión principal (mm) |
| Ancho | Dimensión secundaria (mm) |
| Espesor | Espesor del material (mm) |
| Material | Tipo de material |
| Canto | Bordes con canto aplicado |
| Notas | Observaciones |

## Reglas

- Largo ≥ Ancho (convención).
- Incluir piezas de refuerzo y tapas.
- Fondos: restar 2× espesor lateral + holgura (típico 2–3 mm por lado).
- Cantos: especificar qué bordes llevan canto (frontal, trasero, lateral, todos).

## Exportación

- Guardar como `lista_corte_<proyecto>.csv`.
- Compatible con Excel, Google Sheets, CutList Plus, OptiCut.
- Para importar en CutList Plus: usar formato "CSV with headers".
