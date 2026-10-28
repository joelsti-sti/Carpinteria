# Template — BOM de herrajes y consumibles (CSV)

## Formato CSV

```csv
Item,Cantidad,Especificación,Material,Notas
Bisagra cazoleta 35mm,4,95°,Acero niquelado,Puertas frontales
Corredera telescópica,2 pares,450mm,Acero,Total extension
Tornillo aglomerado,24,4×50mm,Acero zincado,Ensamble general
Clavo acabado,50,1.2×40mm,Acero,Cantos
Canto PVC,10 m,22mm, PVC,Frontales
Neumático gas lift,2,100N,Acero/gas,Puerta abatible
Pegamento,1,250g,PVA,Madera
Lija,3,grano 120,Silicio,Acabado
```

## Columnas

| Columna | Descripción |
|---|---|
| Item | Nombre del herraje/consumible |
| Cantidad | Número de unidades o metros |
| Especificación | Dimensiones, fuerza, ángulo, etc. |
| Material | Material del herraje |
| Notas | Uso, ubicación, observaciones |

## Reglas

- Incluir todos los herrajes, consumibles y acabados.
- Especificar cantidades con margen (agregar 10% para tornillos/clavos).
- Separar herrajes metálicos de consumibles de madera.
- Para soldadura: incluir electrodos, gas, disco de corte.

## Exportación

- Guardar como `bom_<proyecto>.csv`.
- Compatible con Excel, Google Sheets.
- Para presupuesto: agregar columna "Precio unitario" y "Total".
