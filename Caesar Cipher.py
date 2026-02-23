letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1","2","3","4","5","6","7","8","9","10"]
symbols = ["!","@","#","$","%","&","*","?"," "]

def encrypt():
    encrypted_message = ""
    for x in range(len(message)):
        if message[x] in letters:
            n = letters.index(message[x])
            encrypted_message += new_letters[n]
        elif message[x] in numbers:
            n = numbers.index(message[x])
            encrypted_message += numbers[n]
        elif message[x] in symbols:
            n = symbols.index(message[x])
            encrypted_message += symbols[n]
    encrypted_message = "".join(encrypted_message)
    print(f"Encrypted Message = {encrypted_message}")


def decrypt():
    decrypted_message = ""
    for x in range(len(message)):
        if message[x] in new_letters:
            n = new_letters.index(message[x])
            decrypted_message += letters[n]
        elif message[x] in numbers:
            n = numbers.index(message[x])
            decrypted_message += numbers[n]
        elif message[x] in symbols:
            n = symbols.index(message[x])
            decrypted_message += symbols[n]
    decrypted_message = "".join(decrypted_message)
    print(f"Decrypted Message = {decrypted_message}")


choice = "y"
while choice != "n":
    cipher = input("Type 'encode' to Encrypt and 'decode' to Decrypt: ").lower()
    message = input("Type your message: ")
    message = list(message)
    shift = int(input("Enter your shift: "))
    shift = shift % 26
    new_letters = letters[shift:] + letters[:shift]

    if cipher == "encode":
        encrypt()
    elif cipher == "decode":
        decrypt()
    else:
        print("Invalid Input")
    choice = input("would you like to continue? (y/n): ").lower()
