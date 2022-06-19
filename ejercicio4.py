from ejercicio2 import random_generator

def threeArrays(arr1, arr2):

  arr3 = []

  for i in range(len(arr1)):
    for j in range(1):
      sum = arr1[i] + arr2[i]

    arr3.append(sum) 
  
  print("Array 1: ", arr1)
  print("Array 2: ", arr2)
  print("Array 3: ", arr3)

threeArrays(random_generator(1,5, 5), random_generator(10,50, 5))


"""
Explanation: 

1) Declare the array we want to return
2) With a 'For Loop' let's iterate the first array
3) For each iteration, we use the index (i) to get the value in that position of the second array
4) Once we are in the second array and in the (i) index, we get just one item of the array
5) Now, we always are getting, in the same index, 1 item from each array.
6) Then, we sum each other and push it to the empty array previously declared
7) Finally, we use the exercise2's function to generate random arrays 
"""
