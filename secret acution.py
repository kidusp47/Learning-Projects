players = {}
def compare():
    highest = 0
    winner = "Anonymous"
    for i in players:
        bid_amount = players[i]
        if bid_amount > highest :
            highest = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest}")

def play():
    print("\n"*70)
    print("Welcome to the secret acution")
    name = input("What is your name? ")
    if name == "":
        name = "Anonymous"
    bid = int(input("What is your bid? "))
    if bid <=0:
        print("Sorry, that's too low.")
        exit()
    players[name] = bid


choice = "y"
while choice == "y":
    play()
    choice = input("Are there any other bidders? Type (y/n) ")
    print("\n" * 30)
compare()
print("Thank you for playing")

