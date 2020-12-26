while True:
    operator = input("Enter operator : ")
    firstNum = float(input("Enter first number : "))
    secondNum = float(input("Enter second number : "))
    if operator=="+":
       print(firstNum+secondNum)
    elif operator=="-":
       print(firstNum-secondNum)
    elif operator=="*":
        print(firstNum*secondNum)
    elif operator=="/":
        print(firstNum/secondNum)
    else :
        print("Invalid operator!")
