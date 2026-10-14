num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter operator: ")
if operator=="+":
    print(f"The sum of {num1} and {num2} is {num1+num2}")
elif operator=="-":
    print(f"The difference of {num1} and {num2} is {num1-num2}")
elif operator=="*":
    print(f"The multiplication of {num1} and {num2} is {num1*num2}")
elif operator=="/":
    if num2==0:
        print("invalid")
    else:
        print(f"The division of {num1} and {num2} is {num1/num2}")