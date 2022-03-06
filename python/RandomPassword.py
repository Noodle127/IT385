import string
import random

letters = list(string.ascii_letters)
digits = list(string.digits)
special = list(string.punctuation)
characters = list(string.ascii_letters + string.digits + string.punctuation)

def generateRandomPassword():
    length = int(input("Enter password length: "))
    numOfLetters = int(input("Enter desired quantity of letters: "))
    numOfDigits = int(input("Enter desired quantity of digits: "))
    numOfSpecial = int(input("Enter desired quantity of special characters: "))

    total = numOfLetters + numOfDigits + numOfSpecial

    if total > length:
        print("Desired character total is greater than desired password length.")
        return

    password = []

    for i in range(numOfLetters):
        password.append(random.choice(letters))

    for i in range(numOfDigits):
        password.append(random.choice(digits))

    for i in range(numOfSpecial):
        password.append(random.choice(special))

    if total < length:
        random.shuffle(characters)
        for i in range(length - total):
            password.append(random.choice(characters))

    random.shuffle(password)
    print("".join(password))

generateRandomPassword()