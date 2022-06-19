def enterNums():
  numsArr = []

  num = int(input("Enter a number between 0 and 100: "))

  while(num != -1):

    while((num < 0 or num > 100) and num != -1):
      num = int(input("Invalid number. Please, enter a number between 0 and 100: "))  

    if(num != -1):
      numsArr.append(num)
      print(numsArr)
      num = int(input("Please, enter a number between 0 and 100 again: "))      
    elif(num == -1):
      break
        
  print(numsArr)

enterNums()

"""
Explanation:

1) Declare an empty array to store numbers
2) We asked the user for enter the first number
3) If the user enters -1, we just return the empty array
4) Validation of the number entered (must be between 0 and 100). If it's not valid, we ask for the number again
5) Also, thinking in the coming iterations, we validate that the user don't enter -1. If that happens, the program ends.
6) After we finished the program, we want to know the reason. If the program ended because of a valid number entered, we push it to the array and ask the user for another number to add. On the other hand, if the reason was a "-1", we go out and return the array
"""