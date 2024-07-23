import random

number = random.randint(1, 100)
guess = 0
count = 1
while guess != number:

    guess = int(input("Put your guess in right now"))

    if (guess < number):
        print("Guess higher")
        count+=1
    elif (guess > number):
        print("guess lower")
        count+=1
    else:
        print("Nice good job, you got it")
        print("It took you", count, "guesses")
