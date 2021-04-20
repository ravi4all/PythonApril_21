import random

user_score = 0
cpu_score = 0
counter = 0
game = True
while game:
    options = ['stone', 'paper', 'scissor']
    cpu = random.choice(options)

    user = input("Enter your choice : ")
    print("CPU Picked",cpu)
    if user == cpu:
        print("Match Draw")
    elif user == "stone" and cpu == "scissor":
        print("You Win")
        user_score += 1
    elif user == "paper" and cpu == "stone":
        print("You Win")
        user_score += 1
    elif user == "scissor" and cpu == "paper":
        print("You Win")
        user_score += 1

    elif cpu == "stone" and user == "scissor":
        print("You Lose")
        cpu_score += 1
    elif cpu == "paper" and user == "stone":
        print("You Lose")
        cpu_score += 1
    elif cpu == "scissor" and user == "paper":
        print("You Lose")
        cpu_score += 1

    counter += 1
    if counter == 5:
        game = False

print("Final Score : ")
print("User : {}, CPU : {}".format(user_score, cpu_score))

if user_score > cpu_score:
    print("You won the game")
else:
    print("You lose the game")




    
