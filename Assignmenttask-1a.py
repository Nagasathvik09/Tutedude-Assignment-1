#To perform mathematical operations
first_number=int(input("enter the first number:")) #Reading first number dynamically
second_number=int(input("enter the second number:")) #Reading second number dynamically
print("Addition:",first_number+second_number) #Performing addition operation and printing result
print("Subtraction:",first_number-second_number) #Performing subtraction operation and printing result
print("Multiplication:",first_number*second_number) #Performing multiplication operation and printing result
if second_number!=0: #Checking if the second number is not 0
    print("Division:", first_number / second_number) #Performing division operation and printing result only if second number is not 0
else: #If the second number is 0
    print('Division is not possible as denominator is 0') #Printing a message to show division is not possible as denominator is 0