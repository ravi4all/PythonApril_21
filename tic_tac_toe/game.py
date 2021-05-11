import random

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

def userMove(ch):
    pos = int(input("Enter the position : "))
    positions[pos - 1] = ch
    occupied.append(pos)

def cpuMove(ch):
    pos = random.randint(1,9)
    if pos in occupied:
        print("Position already occupied...")
        cpuMove(ch)
    else:
        positions[pos - 1] = ch

def main():
    gameBoard()
    ch = input("Enter your choice : ")
    if ch == "X":
        cpu = '0'
    else:cpu = 'X'
    userMove(ch)
    gameBoard()

    cpuMove(cpu)
    gameBoard()

main()