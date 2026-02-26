def add (a,b):
    result = a+b
    return result
def mul(a,b):
    result = a*b
    return result
def subtract (a,b):
    result = a-b
    return result
def div (a,b):
    result = a/b
    return result

num1 = 0
num2 = 0
exit = False
while exit != True:
    print("----------------------------------------")
    print(f"number 1 = {num1}\nnumber 2 = {num2}")

    print("Menu:") 
    print("1.Add") 
    print("2.Subtract") 
    print("3.Multiply") 
    print("4.Divide")
    print("5.Enter new number")
    print("6.EXIT")

    selection = int(input("Enter choice(1/2/3/4/5/6): "))

    if selection == 1:
        print("----------------------------------------")
        print(f"{num1} + {num2} = {add(num1,num2)}")
    elif selection ==2:
        print("----------------------------------------")
        print(f"{num1} - {num2} = {subtract(num1,num2)}")
    elif selection == 3:
        print("----------------------------------------")
        print(f"{num1} * {num2} = {mul(num1,num2)}")
    elif selection == 4:
        print("----------------------------------------")
        print(f"{num1} / {num2} = {div(num1,num2)}")
    elif selection == 5:
        print("----------------------------------------")
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))
    elif selection == 6:
        print("----------------------------------------")
        print("Goodbye....")
        break

