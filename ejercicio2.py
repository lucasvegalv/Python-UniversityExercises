import random 

def random_generator(a, b, c):
  randomArr = []

  for x in range(c):
    num = random.randint(a, b)
    randomArr.append(num)

  return(randomArr)
  print(randomArr)

"""
Explanation:

1) Create a function which receive three arguments; two are to indicate the range of the numbers we want, and the other argument is to indicate the number of iterations (how many random numbers the loop generates)
2) Declare an empty array to store the numbers
3) With a 'For Loop' we iterate n times, where in each iteration we generate a random number and then we push it to the array previously created.
4) Once the loop finishes, we returned the array with the numbers
5) Finally, we call the function indicating the range and the quantity of numbers that we want
"""