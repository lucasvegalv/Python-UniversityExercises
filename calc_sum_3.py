import random_nums_2

def calcSum():

  arr = random_nums_2.randomNums(1, 5, 5)

  arrLength = len(arr)
  total = 0

  for i in range(arrLength):
    total += arr[i]
    print(total)

  print("El total es: ", total) 

"""
Explanation: 

1) Create a function, which receives and array as arguments
2) Using a 'For Loop', we iterate the array (function's argument) and do the operation
3) Importing and using the function created in the exercise number 2, we call the function

"""