# Input the interval from the user 
startRange = int(input("Enter the start of the interval :"))
endRange = int(input("Enter the end of the interval :"))

print(f"Armstrong numbers in the range {startRange} to {endRange} :")
for i in range(startRange,endRange + 1):
    num_digits = len(str(i)) # Find the number of digits in 'i'
    sum_of_powers = 0
    temp_num = i

    while temp_num > 0:
        digit = temp_num % 10
        sum_of_powers += digit ** num_digits
        temp_num //= 10
         # Check if 'i' is an Armstrong number
    if sum_of_powers == i:
        print(f" {i} /", end="")        
