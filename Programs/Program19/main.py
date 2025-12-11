num = int(input("Enter a number :"))

def armeng (num):
    # Calculate the number of digits in num 
    num_str = str(num)
    num_digits = len(num_str)
    # Initialize variables 
    sum_of_powers = 0 
    temp_num = num

    # Calculate the sum of digits raised to the power of num_digits
    while temp_num > 0:    
        digit = temp_num % 10    
        sum_of_powers += digit ** num_digits    
        temp_num //= 10
    # Check if it's an Armstrong number
    if sum_of_powers == num:    
        output = f"{num} is an Armstrong number."
    else:    
        output = f"{num} is not an Armstrong number."
    
    return output

print(armeng(num))