def calculator1():
    num1 = float(input("first number:"))
    num2 = float(input("second number:"))
    operation = input("enter operation(+,-,*,/):")
    result = 0
    if operation=="+":
        result=num1+num2
        print(result)
    elif operation=="-":
        result = num1-num2
        print(result)
    elif operation=="*":
        result = num1*num2
        print(result)
    elif operation=="/":
        result = num1/num2
        print(result)
    else:
        print("enter valid operation")
        calculator1()
    decision=input("do you want to do new operation?(yes or no):")
    if decision == "yes":
        calculator1()
    elif decision == "no":
            exit("Goodbye")
calculator1()
