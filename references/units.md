# Unidades

## Conversiones básicas

| De | A | Factor |
|---|---|---|
| mm | in | 0.0393701 |
| in | mm | 25.4 |
| cm | in | 0.393701 |
| m | ft | 3.28084 |
| kg | lb | 2.20462 |
| lb | kg | 0.453592 |
| N | lbf | 0.224809 |
| MPa | psi | 145.038 |
| kg/m³ | lb/ft³ | 0.062428 |

## Reglas de redondeo

- Dimensiones de corte: redondear a 0.5 mm (métrico) o 1/32 in (imperial).
- Cargas y fuerzas: redondear a 1 decimal.
- Pesos: redondear a 0.1 kg.
- Porcentajes: redondear a 1 decimal.

## Reglas de trabajo

1. **Unidad primaria:** el usuario elige (métrico por defecto).
2. **Conversión automática:** todos los cálculos internos en métrico (mm, N, MPa, kg/m³).
3. **Salida:** mostrar en la unidad elegida por el usuario, con equivalente entre paréntesis si se solicita.
4. **Tableros/perfiles:** usar medidas estándar de la región del usuario.

## Notación

- Longitudes: mm (métrico), in (imperial).
- Fuerzas: N (métrico), lbf (imperial).
- Presiones: MPa (métrico), psi (imperial).
- Pesos: kg (métrico), lb (imperial).
