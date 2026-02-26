# Program to display Fibonacci sequence using recursion

def fibonacci(n):
    # Base cases: F(0) = 0, F(1) = 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get number of terms from user
terms = int(input("Enter the number of terms: "))

# Check for valid input
if terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    # Display Fibonacci sequence up to requested terms
    for i in range(terms):
        print(fibonacci(i))