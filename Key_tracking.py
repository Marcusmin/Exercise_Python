import pygame
from pygame.locals import *
import sys

pygame.init()

size = width, height = 600, 400
bg = 0, 0, 0
pos = 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Key_tracking")
font = pygame.font.Font(None, 20)
line_height = int(font.get_linesize())
screen.fill(bg)
pygame.key.set_repeat(100, 1)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, pos))
        pos = pos + line_height

        if pos > height:
            pos = 0
            screen.fill(bg)

    pygame.display.flip()



