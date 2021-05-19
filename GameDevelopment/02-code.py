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

h,w = 100, 100
x = width // 2 - w//2
y = height // 2 - h // 2

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # surface - screen, color, [x,y,w,h]
    # pygame.draw.rect(screen, red, [0,0,50,50])
    # pygame.draw.rect(screen, red, [width//2 - 25, height//2 - 25, 50, 50])
    pygame.draw.rect(screen, red, [x, y, w, h])

    pygame.draw.circle(screen, blue, [50,50], 50)

    pygame.display.update()