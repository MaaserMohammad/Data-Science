#---    Q1. Print numbers from 1 to 10 using a for loop. ---

for i in range(1,11):
    print(i)

# --- Q2. Print  Numbers from 1 to n, Display numbers  in increasing order from 1 up to given number n ---

n = int(input("Please tell your number : - "))
for i in range(1,n+1):
    print(i)

# --- Q3. Print  Numbers from 1 to n, Display numbers in decreasing order from given number n down to 1 ---

n = int(input("Please tell your number : - "))
for i in range(n,0,-1):
    print(i)

# --- Q4. Sum of Natural Numbers (1 to n) Take input n and calculate the sum 1 to n ---

n = int(input("Please tell your number : - "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(f"the sum of natural numbers from 1 to {n} is {sum}")

# --- Q5. Factorial of a Number, calculate the factorial(n!) using a loop - multiplying numbers from 1 to n ---

n = int(input("Please tell your number : - "))
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print(f"the factorial of {n} is {factorial}")

# --- Q6. Sum of Odd and Even Numbers in Range, from 1 to n find and print the sum of all even and all odd numbers separately ---

n = int(input("Please tell your number : - "))
sum_even = 0
sum_odd = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i
print(f"the sum of even numbers from 1 to {n} is {sum_even}")
print(f"the sum of odd numbers from 1 to {n} is {sum_odd}")

# --- Q7.  Print all Factors of a Number, Display all numbers that divide the given number exactly(no remainder) ---

n = int(input("Please tell your number : - "))
print(f"the factors of {n} are : - ")
for i in range(1,n+1):
    if n % i == 0:
        print(i)
 
# --- Q8.  Sum of All Factors, Add up all the factors found in the previous question ---

n = int(input("Please tell your number : - "))
sum_factors = 0
for i in range(1,n+1):
    if n % i == 0:
        sum_factors = sum_factors + i
print(f"the sum of factors of {n} is {sum_factors}")


# --- Q9.  Power Calculation(a^b), input base a and exponent b and calculate the result using a loop ---

a = int(input("Please tell your base number : - "))
b = int(input("Please tell your exponent number : - "))
power = 1
for i in range(1,b+1):
    power = power * a
print(f"{a} raised to the power of {b} is {power}")