# --- Ejercicio: Calcular el Área de un Rectángulo ---

# 1. Pedir el largo al usuario y convertirlo a float
largo = float(input("Por favor, introduce el largo del rectángulo: "))

# 2. Pedir el ancho al usuario y convertirlo a float
ancho = float(input("Ahora, introduce el ancho del rectángulo: "))

# 3. Calcular el área
area = largo * ancho

# 4. Mostrar el resultado
print("\n--- Resultados ---") # Añadimos una línea en blanco y un título para que se vea mejor
print("Largo:", largo)
print("Ancho:", ancho)
print("El área del rectángulo es:", area)
print("---------------")