# Fórmulas — Madera

## Flecha de estante (viga)

**Viga simplemente apoyada, carga distribuida uniforme:**
```
δ = (5 × w × L⁴) / (384 × E × I)
```
- w = carga por unidad de longitud (N/mm)
- L = luz (mm)
- E = módulo de elasticidad (MPa = N/mm²)
- I = momento de inercia (mm⁴) = (b × h³) / 12

**Viga empotrada en ambos extremos (fija):**
```
δ = (w × L⁴) / (384 × E × I)
```

**Carga puntual en el centro:**
```
δ = (P × L³) / (48 × E × I)
```

**Límite de flecha:** δ ≤ L/300 (típico para muebles) o L/240 (mínimo aceptable).

## Momento de inercia

- Rectangular: I = (b × h³) / 12
- Sección doble (2 paneles): I = 2 × (b × h³)/12 + A × d² (teorema de ejes paralelos)

## Carga máxima de estante

Despejando w de la fórmula de flecha:
```
w_max = (δ_max × 384 × E × I) / (5 × L⁴)
W_total = w_max × L
```

## Arrancamiento de tornillo (NDS)

```
W = 9.24 × G^1.5 × D^0.5 × L_e
```
- G = gravedad específica de la madera (densidad/1000)
- D = diámetro del tornillo (mm)
- L_e = longitud de penetración efectiva (mm)
- W en N (aplicar factor de seguridad 4–6 para DIY)

## Resistencia de unión con clavos (NDS)

```
Z = (D × L_p × F_e × F_c) / (D + L_p × F_e/F_c)
```
Simplificado: usar tablas de NDS o valores empíricos.

## Neumático (gas lift)

```
F = (P × d_cg) / (d_brazo × sin θ)
```
- F = fuerza del neumático (N)
- P = peso de la puerta (N) = m × 9.81
- d_cg = distancia centro de gravedad al eje (mm)
- d_brazo = longitud del brazo (mm)
- θ = ángulo de apertura (grados)

## Estabilidad (anti-vuelco)

```
Momento estabilizador = W_mueble × (profundidad/2)
Momento vuelco = W_carga × distancia_al_borde
Condición: M_est ≥ 1.5 × M_vuelco
```

## Fuentes

- Timoshenko — Resistencia de Materiales.
- NDS (National Design Specification).
- Eurocódigo 5 (EC5).
- USDA Wood Handbook.
- Confianza: Alta para fórmulas; Media para valores empíricos.
