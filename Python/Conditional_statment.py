# --- Q1. Conditional Statements in Python. Take two user input and determine which one is greater or if they are equal. ---

a = float(input("Please tell the first number: "))
b = float(input("please tell the second number: "))

if a >b:
    print(f"{a} is greater than {b}")
elif b> a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")

