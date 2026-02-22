import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
password = []
final =""

print("Welcome to PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))

for i in range(nr_letters):
    password.append(random.choice(letters))
for i in range(nr_numbers):
    password.append(random.choice(numbers))
for i in range(nr_symbols):
    password.append(random.choice(symbols))
for i in range(len(password)):
    i = random.randint(0,len(password)-1)
    final = final + password[i]
    password.pop(i)
print(f"Your Password is: {final}")