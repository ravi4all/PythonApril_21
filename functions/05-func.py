#Default Arguments
def add(x=0,y=0):
    z = x + y
    print(f"Sum of {x} and {y} is {z}")

add()
add(5)
add(5,6)
add(x=5, y=6)
add(y=6, x=7)
