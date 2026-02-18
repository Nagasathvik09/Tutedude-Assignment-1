ASSIGNMENT 1:
Task 1: Perform Basic Mathematical Operations<br>
PROGRAM:<br>
#To perform mathematical operations<br>
first_number=input("enter the first number:") #Reading first number(string) dynamically<br>
second_number=input("enter the second number:") #Reading second number(string)  dynamically<br>
if first_number.isnumeric() and second_number.isnumeric(): #Checks if all the elements in both the strings are numbers or not<br>
    first_number=int(first_number) #Changes string type to integer type<br>
    second_number=int(second_number) #Changes string type to integer type<br>
    print("Addition:",first_number+second_number) #Performing addition operation and printing result<br>
    print("Subtraction:",first_number-second_number) #Performing subtraction operation and printing result<br>
    print("Multiplication:",first_number*second_number) #Performing multiplication operation and printing result<br>
    if second_number!=0: #Checking if the second number is not 0<br>
        print("Division:", first_number / second_number) #Performing division operation and printing result only if second number is not 0<br>
    else: #If the second number is 0<br>
        print('Division is not possible as denominator is 0') #Printing a message to show division is not possible as denominator is 0<br>
else:<br>
    print("Invalid input")<br>
WORKING:<br>
First I took a variable named first_number and by using input(), I read the number dynamically during execution time as a string.<br>
Same goes with next variable named seconf_number, which can be read dynamically.<br>
After reading ,by using if condition i am checking whether all elements in two strings are numbers or not.<br>
If there are numbers and i am converting them into integer datatype.<br>
Next, I performed addition of first_number and second_number by using (+) operator and then printed its result.<br>
I performed subtraction of first_number and second_number by using (-) operator and then printed its result.<br>
Next, I performed multiplication of first_number and second_number by using (*) operator and then printed its result.<br>
For division, we may have a case of not define answer, when denominator(second_number) becomes 0, so I took if condition to write output for when second_number not equals to 0 , the operation takes place and gets printed,<br>
if the second_number is 0 then "Division is not possible as denominatoris 0" message gets printed.<br>
EXAMPLE: 1<br>
enter the first number:5<br>
enter the second number:10<br>
Addition: 15<br>
Subtraction: -5<br>
Multiplication: 50<br>
Division: 0.5<br>

EXAMPLE: 2<br>
enter the first number:10<br>
enter the second number:0<br>
Addition: 10<br>
Subtraction: 10<br>
Multiplication: 0<br>
Division is not possible as denominator is 0<br>

EXAMPLE: 3<br>
enter the first number:at<br>
enter the second number:9<br>
Invalid input<br>


Task 2: Create a Personalized Greeting<br>
PROGRAM:<br>
#To create a personalized greeting<br>
first_name=input("Enter your first name: ")<br> 
last_name=input("Enter your last name: ")<br> 
print('Hello,',first_name+' '+last_name,'Welcome to the Python program.')<br>
WORKING:<br>
First , I created a variable named first_name and by using input(), I read a string dynamically.<br>
Same ,I created another variable named last_name and by using input(), I read a string dynamically.<br>
Now, I am concatinating two strings by (+) operator.<br>
Here, generally when we concatinate the two strings will join without any gap or space, <br>
so inorder to provide space after writing first_name+ in quotes i am giving space and then again +last_name.<br>
By this the two strings will get concatinated with provided space between them.<br>
EXAMPLE:<br>
Enter your first name: John<br>
Enter your last name: Doe<br>
Hello, John Doe Welcome to the Python program.<br>
