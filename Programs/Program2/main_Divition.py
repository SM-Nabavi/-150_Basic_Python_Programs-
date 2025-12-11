#Divition
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))
if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    divResult = num3 / num4
    print(f"Divition {num3} / {num4} = {divResult}")