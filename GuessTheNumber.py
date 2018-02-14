import sys
import random

number = random.randint(1, 10)
tries = 1

user = input("What is your name? ")

print("Hello", user + ".")

quest = input("Would you like to play a game?[Y/N]")
quest = quest.lower()
print(quest)
while quest != "n" and quest != "y":
    quest = input("Perhaps I wasn't clear enough. Do you wanna play[Y/N]")
    quest = quest.lower()
if quest == "n":
    print("Thats fine, you can play later. Bye for now")
    sys.exit()

if quest == "y":
    guess = int(input("Guess a number from 1 trough 10 "))

while guess < 0 or guess > 10:
    guess = int(input("Please select a number from 1 through 10"))

if guess > number:
    print("Guess lower..")
if guess < number:
    print("Guess Higher...")

while guess != number:
    tries += 1
    guess = int(input("Try guessing again"))

    while guess < 0 or guess > 10:
        guess = int(input("Please select a number from 1 through 10"))

    if guess > number:
        print("Guess lower..")
    elif guess < number:
        print("Guess Higher...")

if guess == number:
    print("Congratulation you guessed correctly. The answer was ", number, ". Your total amount of tries was: ", tries)
