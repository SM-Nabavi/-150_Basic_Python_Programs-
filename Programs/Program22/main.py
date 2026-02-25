# Python Program to find the L.C.M. of two input number

# Getting input from user
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

# Function to calculate Greatest Common Divisor (GCD)
def GCD(a, b):
    # Using absolute values to handle negative numbers
    a, b = abs(a), abs(b)
    
    # Check special cases (when numbers are zero)
    if a == 0:
        return a
    elif b == 0:
        return b
    
    # Repeated subtraction algorithm to calculate GCD
    while a != b:
        if a > b:
            a = a - b  
        else:
            b = b - a  
    return a  

# Function to calculate Least Common Multiple (LCM)
def LCM(a, b):
    # Formula: LCM = |a × b| ÷ GCD(a, b)
    return (abs(a * b) // GCD(a, b))

# Calculate LCM and display the result
result = LCM(num1, num2)
print(f"L.C.M {num1} and {num2} is {result}.")