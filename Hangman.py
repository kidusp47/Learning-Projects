import random
words = ["rhythm", "phlegm", "quiz", "jazzy", "lynx"]
Answer=words[random.randint(0,len(words)-1)]
Answer = list(Answer)
Space = "_"*len(Answer)
Space = list(Space)
round = 0
while (Space != Answer) and round < len(Answer)+1:
    letter = input("Enter a letter: ").lower()
    if letter in Answer:
        n = Answer.index(letter)
        Space[n] = Answer[n]
    elif letter not in Answer:
        round += 1
        print("Round " + str(round))
        if round == len(Answer)+1:
            break
    result = "".join(Space)
    print(result)
if Space == Answer:
    print("You won")
else:
    print("You lost")