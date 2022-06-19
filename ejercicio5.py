def min():

  arr = []
  num = int(input("Please enter a number between 0 and 100: "))
  
  while(num != 0):
    
    while(num < 0 or num > 100):
      num = input("Please enter a valid number: ")

    if(num > 0):
      arr.append(num)

    num = int(input("Please enter another number to add in the list: "))

  min = arr[0]

  for x in range(1, len(arr)):
    if(arr[x] < min): 
      min = arr[x]
      answer = f"The min value of the array is {min} in the {x}º position";
      
  print(arr)
  print(answer)

min()

"""
Explanation: 

1) Initialize an empty array to store the values the user will enter
2) Ask the user for entering a number
3) With a 'While' we validate that the number entered is not 0 so we can start to add numbers to the array
4) Inside the first 'While', we will use another while to validate if the number is between 1 and 100. In case it is not in range, we ask the user for entering the number again until it is valid.
5) Once the user entered a valid number, we have to validate again if it's not equal to 0 (because of the coming iterations). If it's not equal to 0, we push it to the array
6) The last step of the while, once we add the valid number to the array, is to ask the user for entering another number
7) The program ends when the user enters '0'. So, once it happens, we have to do the operations to get the min value of the generated array
8) First, we create a variable to store the min value of the array, and assign it the first element of it. We are assuming the first number is the min so we can compare it with the rest of the elements and change the value if it's necessary
9) With a 'For Loop', we are going to iterate the array, from the second element (the first was already assigned) to the last one.
10) Inside of the loop, we make the main validation: If the current number (arr[x]) is less than the first element of the array, we change the values and the new min is arr[x]. Also, we want the min number's position, so in the answer (inside the for loop) we use 'x' to indicate the index of the current min value
"""
