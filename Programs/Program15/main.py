# The range of finding their prime numbers
lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):  
    flag = True 
    Counter = 0
    
    for i in range(1,num + 1):
        # Checking which numbers a number is divisible by and it must only be divisible by 2 numbers: itself and one.
        if num % i == 0 :
            Counter += 1
        if Counter == 2:
            flag= True
        elif Counter >= 3 or Counter == 1:
            flag = False

    if flag:
        print(num , end=", ")
        

        
