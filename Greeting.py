print("*****- Disneyland ride ticket stand -*****")
name = input("what is your name? ")
age = int(input("what is your age? "))
height = float(input("what is your height?(cm) "))
bill = 0


if height >= 120:
    if age <12 :
        bill = bill + 5
    elif 12 <= age <= 18:
        bill = bill + 7
    else:
        bill = bill + 12

    photo = input("would you like a photo(y/n)")
    if photo == "y":
        bill = bill + 3
    print("your bill is", bill)

else:
    print(f"sorry {name}, you are too short")

