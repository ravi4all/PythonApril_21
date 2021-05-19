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
screen.fill(white)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()