import random
hidden = random.randint(1,20)
while True:
    guess = int(input("ENTER A NUMBER(Number between 1 and 20): "))
    if guess < 1 or guess > 20:
        print("Please enter a valid guess.")
        continue
    if guess == hidden:
        print("Your guess is correct.")
        break
    elif guess < hidden:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")