weight = float(input("Enter your weight: "))

unit = input("Kilograms or pounds (K or L): ")

if unit == "K":
    result = weight * 2.205
    unit = "Lb"
    print(f"Your weight is: {round(result, 1)}{unit}")

elif unit == "L":
    result = weight / 2.205
    unit = "Kg"
    print(f"Your weight is: {round(result, 1)}{unit}")

else:
    print("Invalid unti!")
