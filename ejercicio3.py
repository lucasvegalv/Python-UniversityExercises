from ejercicio2 import random_generator

def calcSum():

  arr = random_generator(1, 5, 5)
  total = 0

  for i in range(len(arr)):
    total += arr[i]

  print("El array generado es: ", arr)
  print("El total es: ", total) 

calcSum()
"""
Explanation: 

1) Create a function, which receives and array as arguments
2) Using a 'For Loop', we iterate the array (function's argument) and do the operation
3) Importing and using the function created in the exercise number 2, we call the function

"""