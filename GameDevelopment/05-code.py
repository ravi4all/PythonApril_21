import pygame
import random
pygame.init()

resolution = width, height = 1000, 500
screen = pygame.display.set_mode(resolution)

# color = (r,g,b) / (red, green, blue) / (0-255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
color_1 = (120,10,45)
clock = pygame.time.Clock()
FPS = 1000

h, w = 50, 50

frog_img = pygame.image.load('frog.png')
frog_img_w = frog_img.get_width()
frog_img_h = frog_img.get_height()

def home():
    font = pygame.font.SysFont(None, 100)
    text = font.render('Welcome to Snake Game', True, black)
    text_2 = font.render('Press SPACE to start game', True, black)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.fill(white)
        screen.blit(text, (100, 100))
        screen.blit(text_2, (100, 200))
        pygame.display.update()

def gameOver():
    font = pygame.font.SysFont(None,100)
    text = font.render('Game Over', True, black)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text, (100, 100))
        pygame.display.update()


def draw_snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen, red, [snakeList[i][0],
                                       snakeList[i][1],
                                       w, h])

def game():
    x, y = 0, 0
    moveX = 0
    moveY = 0

    frog_x = random.randint(0, width - frog_img_w)
    frog_y = random.randint(0, height - frog_img_h)

    snakeList = []
    snakeLength = 1

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 1
                    moveY = 0
                elif event.key == pygame.K_LEFT:
                    moveX = -1
                    moveY = 0
                elif event.key == pygame.K_DOWN:
                    moveY = 1
                    moveX = 0
                elif event.key == pygame.K_UP:
                    moveY = -1
                    moveX = 0

        screen.fill(white)
        snake_rect = pygame.draw.rect(screen, red, [x, y, w, h])
        screen.blit(frog_img, (frog_x, frog_y))
        frog_rect = pygame.Rect(frog_x, frog_y, frog_img_w, frog_img_h)
        x += moveX
        y += moveY

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)

        draw_snake(snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        if frog_rect.colliderect(snake_rect):
            frog_x = random.randint(0, width - frog_img_w)
            frog_y = random.randint(0, height - frog_img_h)
            snakeLength += 20

        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                print("Game over")
                gameOver()

        if x > width:
            x = -w
        elif x < -w:
            x = width

        if y > height:
            y = -h
        elif y < -h:
            y = height
        pygame.display.update()
        clock.tick(FPS)

home()