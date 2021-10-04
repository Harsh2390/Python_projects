print("Welcome to the Basic Calculator")


while True:
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    operation = (input("Choose the operation /, *, +, -: "))
    
    if operation == '+':
        print(x + y)
    elif operation == '*':
        print(x * y)
    elif operation == '-':
        print(x - y)
    elif operation == '/':
        print(x/y)
    else:
        break
        print("thankyou for using calculator")
    
