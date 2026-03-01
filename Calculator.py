def calculator(a,b,operation):
    if operation == "+":
        return f"{a} + {b} = {a + b}"
    elif operation == "-":
        return f"{a} - {b} = {a - b}"
    elif operation == "*":
        return f"{a} * {b} = {a * b}"
    elif operation == "/":
        if b == 0:
            return "Cannot divide by zero"
        else:
            return f"{a} / {b} = {a / b}"
    else:
        print("Invalid operation")
        exit()

a = int(input("Enter a number: "))
operation = input("Enter operation: ")
b = int(input("Enter another number: "))
result = calculator(a,b,operation)
print(result)

choice = "y"
while choice != "n":
    choice = input("Do you want to continue? (y/n): ")
    if choice == "n":
        print(result)
        exit()
    else:
        a = result
        operation = input("Enter operation: ")
        b = int(input("Enter another number: "))
        result = calculator(a,b,operation)
        print(result)
