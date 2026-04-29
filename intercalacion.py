import time
import os


def intercalar(izquierda, derecha, ascendente=True):
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if ascendente:
            if izquierda[i] <= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        else:
            if izquierda[i] >= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


def ordenamiento_intercalacion(lista, ascendente=True):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2

    izquierda = ordenamiento_intercalacion(lista[:mitad], ascendente)
    derecha = ordenamiento_intercalacion(lista[mitad:], ascendente)

    return intercalar(izquierda, derecha, ascendente)


def leer_numeros(nombre_archivo):
    numeros = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if linea != "":
                numeros.append(int(linea))

    return numeros


def guardar_numeros(nombre_archivo, numeros):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for numero in numeros:
            archivo.write(str(numero) + "\n")


def main():
    archivo_entrada = "datos.txt"

    if not os.path.exists(archivo_entrada):
        print("Error: no se encontró el archivo datos.txt")
        print("El archivo debe estar en la misma carpeta que este programa.")
        return

    print("ORDENAMIENTO POR INTERCALACIÓN")
    print("1. Ordenar de menor a mayor")
    print("2. Ordenar de mayor a menor")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        ascendente = True
        archivo_salida = "datos_ordenados_menor_a_mayor.txt"
    elif opcion == "2":
        ascendente = False
        archivo_salida = "datos_ordenados_mayor_a_menor.txt"
    else:
        print("Opción no válida.")
        return

    numeros = leer_numeros(archivo_entrada)

    print(f"\nSe leyeron {len(numeros)} números.")

    inicio = time.perf_counter()

    numeros_ordenados = ordenamiento_intercalacion(numeros, ascendente)

    fin = time.perf_counter()

    guardar_numeros(archivo_salida, numeros_ordenados)

    ruta_guardado = os.path.abspath(archivo_salida)

    tiempo_total = fin - inicio
    tiempo_milisegundos = tiempo_total * 1000

    print("\nOrdenamiento terminado.")
    print(f"Tiempo tardado: {tiempo_milisegundos:.2f} ms")
    print(f"Archivo guardado en: {ruta_guardado}")


if __name__ == "__main__":
    main()