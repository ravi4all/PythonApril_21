import random

cpu = random.randint(0,100)

#q. user will have only 5 chances to guess the number

count = 0
while True:
    guess = int(input("Enter your guess : "))
    if cpu == guess:
        print("Congrats, You guessed the number...")
        break
    elif cpu > guess:
        print("You guessed a smaller number...")
    elif cpu < guess:
        print("You guessed a larger number...")
    else:
        print("Invalid number")

    count += 1
    if count == 5:
        print("You lose the game, Number was",cpu)
        break
