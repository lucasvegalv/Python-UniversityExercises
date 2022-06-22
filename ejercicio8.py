def search(arr, wanted):

  index = 0
  isFounded = False

  while index < len(arr) and not isFounded:
    if(arr[index] == wanted):
      isFounded = True
      return f"The value was founded in the {index + 1}º position"
    else:
      index += 1
    
    if(index == len(arr) and isFounded == False):
      return -1      
  return(isFounded, index)

exampleArr = [2, 4, 6, 10, 1, 100, 50, 23, 40]

"""
Explanation:

1) Declare the function which receives the array and the value we want to find
2) Create two aux variables, 'index' and 'isFounded'. 
3) With a 'While', we will iterate the array under certain conditions. In this case, we are doing 'Linear Search' or 'Sequential Search', so the conditions are: The index variable must be less than the array's length, and the boolean aux variable must be equal to False. If this conditions are true, we keep going
4) Inside the 'While', we are doing and 'If else' statement to validate if the current value is what we want. If it is, we end the 'While' turning the boolean aux variable to True and returning the final answer. If the condition is false, inside the 'else' statement we add one to the index variable (like a 'For Loop')
5) An extra step, is returning a -1 if the wanted value is not in the array. We make this functionality with another 'If else' statement using the length of the array and the value of the boolean variable. This is because if the wanted number is not in the array, the function would return, by default, the last element of the array which is equal to the length of it.
"""