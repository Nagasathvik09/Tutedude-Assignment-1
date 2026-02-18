#To perform mathematical operations
first_number=int(input("enter the first number:"))
second_number=int(input("enter the second number:"))
print("Addition:",first_number+second_number)
print("Subtraction:",first_number-second_number)
print("Multiplication:",first_number*second_number)
if second_number!=0:
    print("Division:", first_number / second_number)
else:
    print('Division is not possible as denominator is 0')