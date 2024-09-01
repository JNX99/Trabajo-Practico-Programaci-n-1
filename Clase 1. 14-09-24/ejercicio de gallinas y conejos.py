gallinas = 0
conejos = 0

for x in range(36):  # rango de 0 a 35, posibles valores para el número de gallinas
    for y in range(36):  # rango de 0 a 35, posibles valores para el número de conejos
        # Verificamos si la combinación cumple con las condiciones
        if x + y == 35 and 2 * x + 4 * y == 94:
            gallinas = x
            conejos = y

print(f"Tienes {gallinas} gallinas y {conejos} conejos.")