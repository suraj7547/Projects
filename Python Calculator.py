operator = input("Enter the operator (+ , - , * , /): ")

num1 = float(input("Enter First Number: "))

num2 = float(input("Enter Second Number: "))

if operator == "+":
    result= num1 + num2

    print(round(result,3))

elif operator == "-":
    result=num1-num2

    print(round(result,3))

elif operator == "*":
    result = num1 * num2

    print(round(result ,3))

elif operator == "/":
    result = num1 / num2

    print(round(result,3))

else:
    print("Invalid operator!")
