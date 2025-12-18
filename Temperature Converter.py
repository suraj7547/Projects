unit = input("Enter The Unit(C/F): ")

temp = float(input("Enter Your Temperature: "))

if unit == "F":
    result = (temp - 32) * 5/9

    print(f"Temperature: {round(result,1)}°C")       #Alt + 0176 = °

elif unit == "C":
    result = (temp * 9/5) + 32

    print(f"Temperature: {round(result,1)}°F")  #Alt + 0176 = °

else:
    print("Invalid Unit!")