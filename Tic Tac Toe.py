import random
options = ["Rock","Paper", "Scissors"]
computer = random.choice(options)
Choice = int(input("Choose your option:0. Rock, 1. Paper, 2. Scissors "))

if (Choice == 0 and computer == "Scissors") or (Choice == 1 and computer == "Rock") or (Choice == 2 and computer == "Paper"):
    print("you Chose: ",options[Choice])
    print("computer Chose: ",computer)
    print("You win!")
elif(Choice == 1 and computer == "Scissors") or (Choice == 2 and computer == "Rock") or (Choice == 0 and computer == "Paper"):
    print("you Chose: ", options[Choice])
    print("computer Chose: ", computer)
    print("You lose!")
else:
    print("you Chose: ", options[Choice])
    print("computer Chose: ", computer)
    print("its a tie!")

