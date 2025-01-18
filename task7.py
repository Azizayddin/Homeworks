import random

secret_number = random.randint(1, 20)
print("I am thinking number between 1 and 20.")

while True:
    guess = int(input("Take a guess: "))
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("congratulations! You guessed the number.")
        break
    