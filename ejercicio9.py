"""Crear tres listas y ordenarlas en forma ascendente utilizando un método para cada lista: métodos de selección, inserción y burbujeo. ¿Qué cambia para ordenar en forma descendente?
"""

array = [5, 2, 10, 8, 7, 1, 3, 6, 9, 4]

# Selection Sort
def selection_sort(arr):
  
  length = len(arr)

  for i in range (length - 1):
    minor = i

    for j in range(i + 1, length):
      if(arr[j] < arr[minor]):
        minor = j

    aux = arr[minor]
    arr[minor] = arr[i]
    arr[i] = aux

  return arr



# Insertion Sort

# Bubble Sort