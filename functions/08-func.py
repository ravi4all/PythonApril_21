def playerHealth():
    health = 67
    return health

def enemyHealth():
    health = 35
    return health

def game():
    p_health = playerHealth()
    e_health = enemyHealth()
    if p_health > e_health:
        print("You are winning")
    else:
        print("You are losing")

game()