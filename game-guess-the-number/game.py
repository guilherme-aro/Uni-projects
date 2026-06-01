# CREATED BY: GUILHERME ARO

# DATE: 04/12/2026

# PROGRAM THAT SIMULATES A NUMBER GUESSING GAME - "GUESS THE NUMBER"



import random



secret_number = random.randint(1, 100)

tries = 0



print("Welcome to the game Guess the Number!")

print("Try to guess a number between 1 and 100")



while True:

    try:

        guess = int(input("Type a guess: "))

    except ValueError:

        print("Please type a valid number!")

        continue



    if guess < 1 or guess > 100:

        print("Your guess must be between 1 and 100!")

        continue



    tries += 1



    if guess < secret_number:

        print("ð¼ Higher!")

    elif guess > secret_number:

        print("ð½ Lower!")

    else:

        print(f"ð Nice one! You got it right in {tries} tries!")

        break

