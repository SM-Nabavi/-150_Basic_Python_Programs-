# Program to convert decimal to binary, octal and hexadecimal

# Convert decimal to binary using repeated division by 2
def bine(a):
    result = ""
    b = a
    if b == 0:  
        return "0"
    while(b > 0):
        remainder = b % 2      # Get binary digit (0 or 1)
        b = b // 2             # Update quotient
        result = str(remainder) + result  # Build number from last to first
    return result

# Convert decimal to octal using repeated division by 8
def octa(a):
    result = ""
    b = a
    if b == 0:
        return "0"
    while(b > 0):
        remainder = b % 8      # Get octal digit (0-7)
        b = b // 8             # Update quotient
        result = str(remainder) + result  # Build number from last to first
    return result

# Convert decimal to hexadecimal using repeated division by 16
def hexa(a):
    result = ""
    b = a
    if b == 0:
        return "0"
    while(b > 0):
        remainder = b % 16     # Get hex digit (0-15)
        b = b // 16            # Update quotient
        
        # Convert 10-15 to A-F
        if remainder == 10:
            char = "A"
        elif remainder == 11:
            char = "B"
        elif remainder == 12:
            char = "C"
        elif remainder == 13:
            char = "D"
        elif remainder == 14:
            char = "E"
        elif remainder == 15:
            char = "F"
        else:
            char = str(remainder)  # Keep 0-9 as digits
        
        result = char + result  # Build number from last to first
    return result

# Get user input and display results
decNum = int(input("Enter the Decimal number: "))
print(f"Binary {decNum} is: {bine(decNum)}")
print(f"Octal {decNum} is: {octa(decNum)}")
print(f"Hexadecimal {decNum} is: {hexa(decNum)}")