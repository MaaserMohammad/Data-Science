# --- Q1. Conditional Statements in Python. Take two user input and determine which one is greater or if they are equal. ---

a = float(input("Please tell the first number: "))
b = float(input("please tell the second number: "))

if a >b:
    print(f"{a} is greater than {b}")
elif b> a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")


# --- Q2. Greet by Gender (male/female) and print a greeting like "Hello Sir" or "Hello Ma'am" ---
# --- Q3. Make the gender check case-insensitive('M','F','m','f' all valid. if input is in valid, print "Wrong input") ---

gen = input("Please tell your gender in Character(m,f) : - ")

if gen == 'm' or gen == "M":
    print("hello sir how are you")
elif gen == "F" or gen == "f":
    print("hello mam how are you ")
else:
    print("wrong input only provide m or f")


# --- Q4. Accept the number from the user and check whether it is even or odd using modulo operator ---

a = int(input("please tell your number:- "))
if a % 2 == 0:
    print("your number is even")
else:
    print("your number is odd ")

# --- Q5. Input name and age. if age => 18, print "eligible to vote". if not , print how many years are left to become eligible ---

name = input("please tell your name:- ")
age = int(input("please tell your age:- "))

if age >= 18:
    print(f"Hello {name} you can vote")
else:
    print(f"Hello {name} sorry you can vote after {18 - age} years")

# --- Q6. Take an integer (1-7) and print the corresponding day of the week. handle invalid input too---

a = int(input("please tell your day(1-7):- "))

if a == 1:
    print("Monday it is")
elif a == 2:
    print("Tuesday it is")
elif a == 3:
    print("Wednesday it is")
elif a == 4:
    print("Thursday it is")
elif a == 5:
    print("Friday it is")
elif a == 6:
    print("Saturday it is")
elif a == 7:
    print("Sunday it is")
else:
    print("sorry your input is wrong")

# --- Q7. Accept three numbers and find the largest among them using nested if-else ---

a = int(input("Please tell your numbers : - "))
b = int(input("Please tell your numbers : - "))
c = int(input("Please tell your numbers : - "))

if a== b and b == c:
    print("all the numbers are equal ")
elif a == b or b == c or c ==a:
    print("any two numbers are equal")
elif a > b and a > c:
    print(f"{a} is the greatest number")
elif b > a and b> c:
    print(f"{b} is the greates number")
else:
    print(f"{c} is the greatest number")

# --- Q8. Input a Year and check if its a leap year using the proper rules:divided by 4, not by 100 unless divisible by400---

year = int(input("please tell your year :- "))

if year % 100 == 0 and year %400 == 0:
    print("its a leap year")
elif year %100 != 0 and year % 4 == 0:
    print("its a leap year ")
else:
    print("sorry its not a leap year")


# --- Q9. Ask for purchase amount and apply discount based on the tresholds: e.g; above 1000 -> 10% off, above 5000 -> 20% off. print final bill.---

bill = int(input("please tell your total amount : - "))

if bill >= 1000 and bill <= 4999:
    print(f"you got a discount of 10% your final amount is {(bill *90)/100}")

elif bill >= 5000:
    print(f"you got a discount of 20% your final amount is {(bill *80)/100}")

else:
    print("sorry no discount for you")

# --- Q10. Accept a single alphabet character and check if it's a vowel(a,e,i,o,u,A,E,I,O,U) or consonant.Also, handle the invalid character ---

char = input("please tell your character : - ")
if char in "aeiouAEIOU":
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")
