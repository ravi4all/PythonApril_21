import pygame
pygame.init()

resolution = width, height = 1000, 500
screen = pygame.display.set_mode(resolution)

# color = (r,g,b) / (red, green, blue) / (0-255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
color_1 = (120,10,45)

h, w = 50, 50
x, y = 0, 0
moveX = 1
moveY = 1
clock = pygame.time.Clock()
FPS = 1000
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.draw.rect(screen, red, [x, y, w, h])
    x += moveX
    y += moveY
    if x > width - w:
        moveX = -1
    elif x < 0:
        moveX = 1

    if y > height - h:
        moveY = -1
    elif y < 0:
        moveY = 1
    pygame.display.update()
    clock.tick(FPS)