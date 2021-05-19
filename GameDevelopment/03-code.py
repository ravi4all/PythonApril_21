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
screen.fill(white)

h, w = 50, 50

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for i in range(10):
        for j in range(i+1):
            pygame.draw.rect(screen, red, [j * 51, i * 51, w, h])

    pygame.display.update()