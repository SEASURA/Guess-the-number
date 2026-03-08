import random

secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("🎉 Amazing! You guessed it right!")
    print("You are very smart! 😎")
elif guess > secret_number:
    print("Oops! Too high.")
    print("But nice try, keep going! 👍")
else:
    print("Oops! Too low.")
    print("Good effort! Try again next time 💪")

print("The correct number was:", secret_number)