import random

win_conditions = [[0,1,2],[3,4,5],[6,7,8],
                  [0,3,6],[1,4,7],[2,5,8],
                  [0,4,8],[2,4,6]]

positions = list(range(1,10))
occupied = []
def gameBoard():
    print("""
        {} | {} | {}
       ------------
        {} | {} | {}
       ------------
        {} | {} | {}
    """.format(positions[0],positions[1],positions[2],
               positions[3],positions[4],positions[5],
               positions[6],positions[7],positions[8]))

def checkWinner(pos,ch):
    for i in range(len(win_conditions)):
        if pos in win_conditions[i]:
            index = win_conditions[i].index(pos)
            win_conditions[i][index] = ch

    for i in range(len(win_conditions)):
        if win_conditions[i][0] == ch and win_conditions[i][1] == ch and win_conditions[i][2] == ch:
            return "{} Win".format(ch)

def userMove(ch):
    pos = int(input("Enter your position : "))
    index = pos - 1
    occupied.append(index)
    positions[index] = ch
    gameBoard()
    msg = checkWinner(pos,ch)
    if msg:
        return True

def cpuMove(ch):
    pos = random.randint(1,9)
    print("CPU Picked : ",pos)
    if pos in occupied:
        cpuMove(ch)
    index=  pos - 1
    positions[index] = ch
    gameBoard()
    msg = checkWinner(pos,ch)
    if msg:
        return True


def main():
    gameBoard()
    user_ch = input("Enter your choice : 0 or X : ")
    if user_ch == "X":
        cpu_ch = '0'
    else: cpu_ch = 'X'

    while True:
        if userMove(user_ch):
            print("User win")
            break
        if cpuMove(cpu_ch):
            print("CPU Win")
            break

main()