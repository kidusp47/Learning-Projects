print("*****- Welcome to python Pizza Deliveries!!! -*****")
size = input("What size pizza do you want?(S, M, OR L)").upper()
pepperoni = input("Do you want pepperoni?(Y/N)").upper()
extra_cheese = input("Do you want extra cheese?(Y/N)").upper()
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

else:
    print("Please enter a valid size")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print("Your bill is", bill)



