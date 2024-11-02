import random

numbers = [2, 4, 7, 9, 11, 13, 16, 19, 21, 23]
judge = random.choice(numbers)
print(numbers)
guess = int(input("Guess the number: "))
if guess == judge:
    print("You got it!")
else:
    if guess < judge:
        print("Your guess is less. Try again.")
    else:
        print("Your guess is greater. Try again.")
    