def students():
  
  monthsCont = [0]*12
  legNum = int(input('Please enter the student credential number so you can enter the birthday: '))

  while(legNum != -1):
    
    birthDay = int(input('Please enter the day of your birthday: '))
    while(birthDay < 1 or birthDay > 31):
      birthDay = int(input('Please enter the day of your birthday: '))

    birthMonth = int(input('Please enter the month of your birthday: '))
    while(birthMonth < 1 or birthMonth > 12):
      birthMonth = int(input('Please enter the month of your birthday: '))
    

    birthYear = int(input('Please enter the year of your birthday: '))
    while(birthYear < 1800 or birthYear > 2020):
      birthYear = int(input('Please enter the year of your birthday: '))

    if(birthMonth == 1):
      monthsCont[0] = monthsCont[0] + 1
    elif(birthMonth == 2):
      monthsCont[1] = monthsCont[1] + 1
    elif(birthMonth == 3):
      monthsCont[2] = monthsCont[2] + 1
    elif(birthMonth == 4):
      monthsCont[3] = monthsCont[3] + 1
    elif(birthMonth == 5):
      monthsCont[4] = monthsCont[4] + 1
    elif(birthMonth == 6):
      monthsCont[5] = monthsCont[5] + 1
    elif(birthMonth == 7):
      monthsCont[6] = monthsCont[6] + 1
    elif(birthMonth == 8):
      monthsCont[7] = monthsCont[7] + 1
    elif(birthMonth == 9):
      monthsCont[8] = monthsCont[8] + 1
    elif(birthMonth == 10):
      monthsCont[9] = monthsCont[9] + 1
    elif(birthMonth == 11):
      monthsCont[10] = monthsCont[10] + 1
    else: 
      monthsCont[11] = monthsCont[11] + 1
    
    maxMonthCont = monthsCont[0]
    maxMonthIndex = 0
    for i in range(1, len(monthsCont)):
      if(monthsCont[i] > maxMonthCont):
        maxMonthCont = monthsCont[i]
        maxMonthIndex = i

    legNum = int(input('Please enter another student credential number so you can enter the birthday: '))

  print(f"Enero: {monthsCont[0]}")
  print(f"Febrero: {monthsCont[1]}")
  print(f"Marzo: {monthsCont[2]}")
  print(f"Abril: {monthsCont[3]}")
  print(f"Mayo: {monthsCont[4]}")
  print(f"Junio: {monthsCont[5]}")
  print(f"Julio: {monthsCont[6]}")
  print(f"Agosto: {monthsCont[7]}")
  print(f"Septiembre: {monthsCont[8]}")
  print(f"Octubre: {monthsCont[9]}")
  print(f"Noviembre: {monthsCont[10]}")
  print(f"Diciembre: {monthsCont[11]}")
  print(f"El mes con mayor cantidad de cumpleañeros es el mes: {maxMonthIndex + 1}, con un total de {maxMonthCont} cumpleañeros")

students()

"""
Explanation: 

1) We will use numbers to indicate the months instead of its names, so we declare an array with 12 elements with the value of 0. This number is to store the amount of birthdays for each month. Then, we will use the index of each element to make reference to the month we want
2) Ask the user for entering the 'legajo' so he/she can enter the birthday's values
3) If the 'legajo' is equal to -1, the program ends. If it's different to -1, the user starts the main program
4) The main program is the data inputs to store the different students's birthdays, so inside a 'While' we aske the user for entering the data and also we make the validation to make sure the days, months, and years are valid. In case they are not, we will ask the user again until the data is valid
5) Once the user enter all the data, we hardcoded the month counter (because we are not using objects and also we dont have a 'Switch' statement). The month counter is basically counting how many students were born in each month.
6) Once we added 1 to the month, we ask the user for entering another 'legajo' so he/she can continue with the program. In case the user enters -1, the program ends and we print the months with its values and the final answer.
"""