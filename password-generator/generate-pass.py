import time
import random as ra

capAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallAlpha = capAlpha.lower()
specialChars = "!@#$%^&*()_-=+}{][:;.,<>`~/?\\\" "
numberChars = "1234567890"

def generate(userlength, userSpecialChar):
    userGeneratedPassword = []
    itemsWithSpecialChars = {1: capAlpha, 2: smallAlpha, 3: specialChars, 4: numberChars}
    items = {1: capAlpha, 2: smallAlpha, 3: numberChars}

    if (userSpecialChar.lower() == 'y'):
        for _ in range(0, int(userlength)):
            userGeneratedPassword.append(ra.choice(ra.choice(list(itemsWithSpecialChars.values()))))
    else:
        for _ in range(0, int(userlength)):
            userGeneratedPassword.append(ra.choice(ra.choice(list(items.values()))))

    hasUpper = any(char.isupper() for char in userGeneratedPassword )
    hasLower = any(char.islower() for char in userGeneratedPassword )
    hasDigit = any(char.isdigit() for char in userGeneratedPassword )
    hasSpecialChar = any(char in specialChars and userSpecialChar for char in userGeneratedPassword )
    if hasDigit and hasLower and hasUpper:
        if userSpecialChar.lower() == 'n' or hasSpecialChar:
            return ''.join(userGeneratedPassword)

def main():

    while True:
        userlength = input("Enter length of your password: ")

        if userlength.isdigit():
            break

        print("Please enter a valid digit!")

        if (userlength.lower() == "quit"):
            break


    # Validate special character preference
    while True:
        userSpecialChar = input("Would you like special characters (Y/N)?: ")

        if userSpecialChar.lower() in ('y', 'n'):
            break

        print('Please enter either "Y" or "N"')

    print("Generating... ")
    time.sleep(2)
    generatedPassword = generate(userlength, userSpecialChar)
    print(f'Your generated password is: "{generatedPassword}"')

main()