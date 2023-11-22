from random import randint

def get_valid_guess():
    while True:
        guess = input("What number am I thinking of? ")
        try:
            guess = int(guess)
            if 1 <= guess <= 99:
                return guess
            else:
                print("Please enter a number between 1 and 99.")
        except ValueError:
            print("Please enter a valid number.")

secret_number = randint(1, 99)
while True:
    guess = get_valid_guess()
    if secret_number == guess:
        print("Yay! You got it.")
        break
    elif secret_number > guess:
        print("No, that's too low.")
    else:
        print("No, that's too high.")