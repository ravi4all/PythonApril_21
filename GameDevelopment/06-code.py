import pygame

pygame.init()

resolution = width, height = 1000, 500
screen = pygame.display.set_mode(resolution)

# colour = ( r , g , b) /( Red, Green, Blue ) / (0-255)

red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
colour_1 = (110, 61, 45)
moveX = 1
screen.fill(red)

h, w = 50, 50
x, y = 0, 0
moveX = 0
moveY = 0
clock = pygame.time.Clock()
FPS = 1000

while True:
    for event in pygame.event.get():
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
    pygame.draw.rect(screen, green, [x, y, w, h])
    x += moveX
    y += moveY
    if x > width:
        x = -50
    elif x < -50:
        x = width

    if y > height:
        y = -50
    elif y < -50:
        y = height

    pygame.display.update()
    clock.tick(FPS)