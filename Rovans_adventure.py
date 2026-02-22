import random

print("*****- ⚔️SHADOWS OF THE IRON REALM⚔️ -*****\n\n")
print("You are Rovan, a wandering adventurer entering the forbidden land known as The Iron Realm.")

Health = 100
Gold = 50
Honor = 50
Fear = 0
Inventory = []

choice = ''

print(f"You start with Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")

print('''
Goal
🗡️ Find the Crown Of Ashes
🗡️ Escape alive

Lose If
☠️ Health ≤ 0
☠️ Fear ≥ 100
☠️ Honor ≤ 0
''')

print("🌲 CHAPTER 1 – THE FORKED ROAD")
print("\nHello Adventurer you seem to have reached a forked road. Choose a path")
print("A) Take the Dark Forest\nB) Take the Mountain\nC) Camp and scount first")
choice = input("your Choice Adventurer?(A,B,C) ").upper()
if choice == 'A':
    Health -= 20
    Gold += 30
    Fear += 20
    Inventory.append("Strange Amulet")
    print("\nAdventurer it seemed you had Aquired a amulet.")
    print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory[0]}")
elif choice == 'B':
    Bandit_ambush = random.randint(1, 10)
    if 1 <= Bandit_ambush <= 4:
        print("🏹 CHAPTER 2 – BANDIT AMBUSH")
        print("Adventurer it Seems you are surrounded by 3 bandits")
        print("Hurry chooses what acttion you will take: \nA)Fight\nB)Bribe them\nC)Intimidate them")
        choice = input("your Choice Adventurer?(A,B,C) ").upper()
        if choice == 'A':
            if Health > 60:
                Gold += 50
                Honor += 15
                Health -= 30
            else:
                Health -= 50
        elif choice == 'B':
            Gold -= 40
            Honor -= 10
        elif choice == 'C':
            Success = random.randint(1, 10)
            if Success <= 5:
                Honor += 20
            else:
                Health -= 25
        else:
            Health -= 30
            Gold -= 30
            Honor -= 50
            Fear += 30

        print("\nYou Survived being  ambushed by bandits Adventure im glad your still with us.")
        print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
    else:
        Health -= 10
        Honor += 10
        print("\nAdventurer you gain honor for this challenging path.")
        print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
elif choice == 'C':
    Bandit_ambush = random.randint(1, 10)
    if 1 <= Bandit_ambush <= 2:
        print("🏹 CHAPTER 2 – BANDIT AMBUSH")
        print("Adventurer it Seems you are surrounded by 3 bandits")
        print("Hurry chooses what acttion you will take: \nA)Fight\nB)Bribe them\nC)Intimidate them")
        choice = input("your Choice Adventurer?(A,B,C) ").upper()
        if choice == 'A':
            if Health > 60:
                Gold += 50
                Honor += 15
                Health -= 30
            else:
                Health -= 50
        elif choice == 'B':
            Gold -= 40
            Honor -= 10
        elif choice == 'C':
            Success = random.randint(1, 10)
            if Success <= 5:
                Honor += 20
            else:
                Health -= 25
        else:
            Health -= 30
            Gold -= 30
            Honor -= 50
            Fear += 30

        print("\nYou Survived being  ambushed by bandits Adventure im glad your still with us.")
        print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
    else:
        Health += 10
        Gold -= 10

        print("\nAdventurer you gain honor for this challenging path.")
        if Health > 100:
            Health = 100
        print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
else:
    Health -= 20
    Honor -= 20
    print("\nSeems like this Adventurer is a Coword 😂.")
    print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
    print("\n\n")

print("🏰 CHAPTER 3 – THE ABANDONED CASTLE")
print(
    "\nYou find the ruined castle rumored to hold the Crown.\n\nInside you discover a trapped hallway.\nHow will you over this Challenge Adventurer")
print("A) Rush Through\nB) Disarm traps Carefully\nC) Turn Back")
choice = input("your Choice Adventurer?(A,B,C) ").upper()
if choice == 'A':
    success = random.randint(1, 10)
    if success <= 5:
        Health -= 40
        print("it seems you injured your leg Adventurer")
    else:
        print("it Cant belive that worked you one lucky adventurer")
    print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
elif choice == 'B':
    if "Strange Amulet" in Inventory:
        print("its A Good thing you have that Amulet")
    else:
        Health -= 20
    print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
elif choice == 'C':
    Fear += 10
    Honor = 0
    Health = 0
    print("\nMay you live in Shame as long as you draw breath")
    print("🏁 ENDINGS")
    print("this mark the tail of the Clown Adventurer. whose back only knows Scars. because of his Cowerdly retreat")
    print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
    exit()
else:
    Honor = 0
    Health = 0
    print("\nIt seems your inaction lead for the hallway to collapse")
    print("🏁 ENDINGS")
    print("this mark the tail of the Indecisive Adventurer. who when needed the most couldnt Accomplish anything.")
    print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
    exit()

print("🐉 CHAPTER 4 – THE SHADOW BEAST")
print("Guarding the Crown is a shadow creature. What will you do Adventurer")
print("A) Fight\nB) Use Strange Amulet\nC) Attempt ot steal Crown Silently")
choice = input("your Choice Adventurer?(A,B,C) ").upper()
if choice == 'A':
    if Health > 50 and Fear < 50:
        print("You Safely Retrived the Crown Adventurer")
    else:
        Health = 0
        print("You Have Died Adventurer")
elif choice == 'B':
    if "Strange Amulet" in Inventory:
        print("The Beast has weakend you Have done it")
        Health -= 20
    else:
        print("You Have Died Adventurer")
else:
    success = random.randint(1, 10)
    if success <= 3:
        print("You Have Silently reterived the Crown Adventurer")
    else:
        if Health > 50 and Fear < 50:
            print("You Safely Retrived the Crown Adventurer")
        else:
            Health = 0
            print("You Have Died Adventurer")

print("🏁 ENDINGS")
print(f"Health: {Health} \n Gold: {Gold} \n Fear: {Fear} \n Honer: {Honor} \n Inventory: {Inventory}")
if Honor >= 70:
    print("You should always be Proclaimed as 🏆 Hero of the Realm")
elif Fear >= 100:
    print("You should always be Proclaimed as 🕳Lost in Darkness")
elif Fear >= 70:
    print("You should always be Proclaimed as 🩸 Cursed Wanderer")
elif Health <= 0:
    print("You should always be Proclaimed as ☠ Fallen Adventurer")
