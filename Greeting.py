weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are under weight")
elif bmi >= 18.5 and bmi <= 24.5:
    print("You are normal Weight")
else:
    print("You are over weight")