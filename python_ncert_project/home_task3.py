"""Write a program to input the value of x and n nad print the sum 
of following series"""

""" 1 + x + x² + x³ + x⁴ +..... + xⁿ  """
n=int(input("Enter value of n:"))
x=int(input("Enter value of x:"))
total=1
for i in range(1,n+1):
    total+=pow(x,i)
print("The sum of the series :",total)


# """ 1 - x + x² - x³ + x⁴ - ...... - xⁿ """   # 1 + (-x)¹ + (-x)² + (-x)³ + (-x)⁴ +...

n=int(input("Enter value of n:"))
x=int(input("Enter value of x:"))
total=1
for i in range(1,n+1):
    total+=pow(-x,i)
print("The sum of the series :",total)



""" x - x²/2 + x³/3 - x⁴/4 +...... xⁿ/n """ # -{ -x + x²/2 - x³/3 + x⁴/4...}  ==> # - { (-x) + (-x)²/2 + (-x)³/3 +......}
                                                
n=int(input("Enter value of n:"))
x=int(input("Enter value of x:"))
total=0
for i in range(1,n+1):
    total+= - pow(-x,i)/i
print("The sum of the series :",total)



""" x + x²/2! - x³/3! + x⁴/4! - ....xⁿ/n! """

import math

# Input values
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms n: "))

# Initialize sum
sum_series = 0

# Loop through terms from 1 to n
for i in range(1, n + 1):
    sign = (-1) ** (i + 1)  # Alternating sign: + - + - ...
    term = sign * (x ** i) / math.factorial(i)
    sum_series += term

# Print the result
print(f"The sum of the series is: {sum_series}")


