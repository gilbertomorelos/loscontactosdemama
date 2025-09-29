import csv

# Nombre del archivo
archivo = "numeros.csv"

# Crear archivo con columna "telefono"
with open(archivo, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Escribir encabezado
    writer.writerow(["telefono"])

    # Aquí puedes agregar los números manualmente como ejemplo
    numeros_ejemplo = [
        "4421697170",
        "4423586523",
        "4427113770"
    ]

    # Escribir números en el archivo
    for numero in numeros_ejemplo:
        writer.writerow([numero])

print(f"Archivo '{archivo}' creado. Agrega tus números en la columna 'telefono'.")
