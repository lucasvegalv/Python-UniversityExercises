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

"""
Explanation: 

1) In a function, which receives an array as argument, we use a 'For Loop' to iterate through the array. The first loop iterates from the first element to the penultimate. 
2) In order to be able to compare the elements, we will store the first element's position in a variable called 'minor' (because until we find an element less than it, the first one is the minor)
3) Then, we hav to iterate the array again but this time we it goes from the 'i + 1' position (always one more than the first iteration) to the last element of the list. 
4) Now that we have an element and the next one, we can compare each other. We do this using an 'If else' statement where we check if the elements in the 'j' position (second iteration) are less than the element in the 'i' position (the first iteration).
5) In each iteration (the second one) we make the conditional statement. If that check is True, we will make change between the elements. We will want to move the arr[j] element to the 'i' position, and the arr[i] element to the 'j' position. That's what we do in line 13º, where the 'minor' variable is 'j' now.
6) Now that we change the minor position value, the last step is to exchange the values. In order to do this, we need an aux/temporary variable to store one of the two values (this is because once we replace its value, we lose it. But we want to use that value later, so we have to store it). 
"""

# Bubble Sort

def bubble_sort(arr):

  for i in range(len(arr) - 1):
    
    for j in range(len(arr) - 1):
      if(arr[j] > arr[j + 1]):        
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
      
  return arr

print(bubble_sort(array))
    
    



"""
Explanation:

1) For this sort algorithm we have to use a 'For Loop' to indicate how many times we want to make the main operation (compare each element with its next one).
2) Once we have the first loop, we need another 'For Loop' to make this comparison operations we said. Inside of it, we will check if the first element is greater than the next one. 
3) If that is true we exchange the values (this time, we use multiple assignment but the idea is the same; we need to store a value in a temporary variable so we don't lose it after we change the values)
4) Finally we return the ordered array
5) As we could see, this method is not the most efficient because it needs a lot of iterations (the length of the array - 1 ^ 2), comparisons, position's changes in each iteration, etc.
"""

# Insertion Sort





