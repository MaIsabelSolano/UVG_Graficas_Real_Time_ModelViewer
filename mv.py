import random
import pygame

pygame.init()

screen = pygame.display.set_mode((1600, 1200))

running = True


while (running):
    x = random.randint(0, 1600)
    y = random.randint(0,1200)
    screen.set_at((x, y), (255, 255, 255))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False