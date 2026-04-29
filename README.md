# wiki-Benchmark-inter
# Ordenamiento por Intercalación - Merge Sort

## Descripción

Este tarea implementa el algoritmo de ordenamiento por **Intercalación**, también conocido como **Merge Sort**, utilizando Python.

El programa lee un archivo llamado `datos.txt`, el cual debe estar en la misma carpeta que el archivo `.py`. Este archivo contiene una lista de números, uno por línea. Después, el programa pregunta al usuario si desea ordenar los datos de **menor a mayor** o de **mayor a menor**.

Al finalizar, el programa muestra el tiempo que tardó el ordenamiento en **milisegundos** y guarda los datos ordenados en un archivo nuevo.

---

## ¿Cómo funciona el algoritmo?

El algoritmo de Intercalación trabaja con la estrategia de **dividir y vencer**.

Primero divide la lista original en dos mitades. Después, cada mitad se vuelve a dividir en partes más pequeñas hasta llegar a listas de un solo elemento. Luego, esas listas pequeñas se van uniendo nuevamente, pero ahora de forma ordenada.

Por ejemplo:


Lista original:
[8, 3, 5, 1]

Se divide:
[8, 3] [5, 1]

Se vuelve a dividir:
[8] [3] [5] [1]

Se intercalan ordenadamente:
[3, 8] [1, 5]

Resultado final:
[1, 3, 5, 8]

### Análisis de complejidad ###

El algoritmo de ordenamiento por Intercalación, también conocido como Merge Sort, tiene una complejidad de:

**O(n log n)**

Esto se debe a que el algoritmo divide la lista en mitades varias veces hasta llegar a listas de un solo elemento. Esa división genera aproximadamente `log n` niveles. Después, en cada nivel, se realiza la intercalación de los elementos, recorriendo todos los datos, lo cual tiene un costo de `O(n)`.

Por eso, la complejidad total se expresa como:

**O(n log n)**

# Mejor caso

**O(n log n)**

Aunque la lista ya esté ordenada, el algoritmo de Intercalación sigue dividiendo la lista y uniendo sus partes nuevamente, por lo que mantiene la misma complejidad.

# Caso promedio

**O(n log n)**

Este es el comportamiento normal del algoritmo cuando los datos están en un orden aleatorio.

# Peor caso

**O(n log n)**

Aunque los datos estén completamente desordenados, el algoritmo mantiene un rendimiento estable, ya que siempre divide e intercala de la misma manera.

### Complejidad espacial

**O(n)**

El algoritmo necesita memoria adicional para almacenar las listas temporales que se generan durante el proceso de intercalación.
## Comparativa teórica contra Bubble Sort

El ordenamiento por Intercalación o Merge Sort es más eficiente que Bubble Sort cuando se trabaja con una gran cantidad de datos. Merge Sort utiliza la estrategia de dividir y vencer, separando la lista en partes más pequeñas y después uniéndolas de forma ordenada. En cambio, Bubble Sort compara elementos vecinos e intercambia sus posiciones si están en el orden incorrecto.

En cuanto a complejidad, Merge Sort tiene un rendimiento de **O(n log n)** en el mejor caso, caso promedio y peor caso. Por otro lado, Bubble Sort tiene una complejidad promedio y peor caso de **O(n²)**, por lo que se vuelve mucho más lento cuando aumenta la cantidad de elementos.

Una ventaja de Bubble Sort es que es más fácil de entender e implementar. Sin embargo, para listas grandes, como una lista de 50,000 números, Merge Sort es una mejor opción porque mantiene un rendimiento más estable y rápido.
