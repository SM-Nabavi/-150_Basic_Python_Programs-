# Calculate BMI using formula weight/height²
def bmi(w,h):
    return round(w / h**2,2)

# Get user input
Weight = float(input("Enter your weight in kg: "))
Height = float(input("Enter your height in meters: "))

# Calculate and display BMI
meBMI = bmi(Weight,Height)
print(f"Your BMI is: {meBMI}")

# Classify based on BMI categories
if meBMI <= 18.5:
    print("You are underweight.")
elif 18.5 < meBMI <= 24.9:
    print("Your weight is normal.")
elif 25 < meBMI <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")