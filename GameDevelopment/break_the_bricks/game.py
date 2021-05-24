import pygame
pygame.init()

resolution = width, height = 1000, 500
screen = pygame.display.set_mode(resolution)

# color = (r,g,b) / (red, green, blue) / (0-255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
blue = (0,255,0)
color_1 = (120,10,45)

def score(s):
    font = pygame.font.SysFont(None, 30)
    text = font.render('Score : {}'.format(s), True, red)
    screen.blit(text,(10,10))

def life_remaining(life):
    font = pygame.font.SysFont(None, 30)
    text = font.render('Life Remaining : {}'.format(life), True, red)
    screen.blit(text, (300, 10))

def gameOver():
    pass

def main():
    bar_width = 200
    bar_height = 15
    barX = width // 2 - bar_width // 2
    barY = height - 20
    moveBarX = 0

    ballRadius = 7
    # ballX = barX + bar_width // 2
    ballY = barY - ballRadius
    moveBallX = 0
    moveBallY = 0
    moveBall = False

    brick_width = 100
    brick_height = 30
    n_rows = 5
    n_cols = width // brick_width

    bricks = []
    for i in range(1,n_rows+1):
        for j in range(n_cols):
            brick_x = (brick_width + 5) * j
            brick_y = (brick_height + 5) * i
            brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
            bricks.append(brick)

    FPS = 200
    clock = pygame.time.Clock()

    s = 0
    life = 3

    while True:
        if not moveBall:
            ballX = barX + bar_width // 2
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveBarX = 1
                elif event.key == pygame.K_LEFT:
                    moveBarX = -1
                elif event.key == pygame.K_SPACE:
                    moveBallX = 1
                    moveBallY = -1
                    moveBall = True
            else:
                moveBarX = 0

        screen.fill(white)

        barRect = pygame.draw.rect(screen, red, [barX, barY, bar_width, bar_height])
        barX += moveBarX
        ballX += moveBallX
        ballY += moveBallY

        for i in range(len(bricks)):
            pygame.draw.rect(screen, color_1, bricks[i])

        pygame.draw.circle(screen, black, [ballX, ballY], ballRadius)
        ballRect = pygame.Rect(ballX, ballY, ballRadius, ballRadius)
        for i in range(len(bricks)):
            if bricks[i].colliderect(ballRect):
                moveBallY = 1
                FPS += 10
                s += 1
                del bricks[i]
                break

        if ballY > height * 3:
            ballY = barY - ballRadius
            moveBall = False
            moveBallX = 0
            moveBallY = 0
            life -= 1
        elif ballY < ballRadius:
            moveBallY = 1
        elif ballX > width - ballRadius:
            moveBallX = -1
        elif ballX < ballRadius:
            moveBallX = 1
        elif ballRect.colliderect(barRect):
            moveBallY = -1

        if life == 0:
            gameOver()

        score(s)
        life_remaining(life)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()