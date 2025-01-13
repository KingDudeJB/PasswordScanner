#https://www.youtube.com/watch?v=iJ01q-sRJAw
#https://www.youtube.com/watch?v=KCWWL54He_g
#https://www.youtube.com/watch?v=Evwrt2q5vqw

#Python Standard Library:
    #string module
    #tkinter
#Best Practices in Programming:
#Common Python Practices:

import string

def PWC(password):
    # Check for different character types in the password
    upper_case = any(c in string.ascii_uppercase for c in password)  # looking for upper case letters
    lower_case = any(c in string.ascii_lowercase for c in password)  # looking for lower case letters
    special = any(c in string.punctuation for c in password)  # looking for special characters
    digits = any(c in string.digits for c in password)  # looking for digits

    # Create a list of boolean values indicating the presence of character types
    characters = [upper_case, lower_case, special, digits]
    length = len(password)
    score = 0

    # Check if password is in the common passwords list
    try:
        with open('E:/Cyber Security Work/Common Passwords.txt', 'r') as f:
            common = f.read().splitlines()

        if password in common:
            print(f"Password found in common list. Score: 0 / 7")
            return "Password found in common list. Score: 0 / 7"
    except FileNotFoundError:
        print("Common passwords file not found. Proceeding with scoring...")

    # Add points based on password length
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    print(f"Password length is {length}, adding {score} points!")

    # Add points based on diversity of character types
    character_types = sum(characters)  # Number of different character types present
    score += max(0, character_types - 1)  # Add points based on the number of character types

    print(f"Password has {character_types} different character types, adding {max(0, character_types - 1)} points!")

    # Final score evaluation
    if score < 4:
        return f"The password is quite weak! Score: {score} / 7"
    elif score == 4:
        return f"The password is okay! Score: {score} / 7"
    elif 4 < score < 6:
        return f"The password is pretty good! Score: {score} / 7"
    else:
        return f"The password is strong! Score: {score} / 7"
