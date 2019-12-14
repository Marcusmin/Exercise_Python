import pygame
from pygame.locals import *
import sys

pygame.init()

size = width, height = 800, 600
bg = 255, 255, 255
running = True
position = [0, 0]
speed = 1
fullscreen = False
degree = 45
#return出surface
screen = pygame.display.set_mode(size, RESIZABLE)
#加载图像素材
image_man = pygame.image.load(r'C:\Users\未来人类\Desktop\PYTHON\material\image\charcater\man.png')
#转换图像大小
man = pygame.transform.smoothscale(image_man, (40, 30))


#窗口标题
pygame.display.set_caption("It's my war")
#rect-move
man_rect = man.get_rect()

while running:
    for event in pygame.event.get():
        #KEYDOWN 检测按键
        if event.type == KEYDOWN:
#            degree *= -1
#            man = pygame.transform.rotate(man, degree)

            #检测ESC
            if event.key == K_ESCAPE:
                running = False
            #方向控制
            if event.key == K_w:
                position[1] = -1 * speed
            if event.key == K_a:
                position[0] = -1 * speed
            if event.key == K_s:
                position[1] = 1 * speed
            if event.key == K_d:
                position[0] = 1 * speed
            #全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((800, 600), FULLSCREEN | HWSURFACE)
                else:
                    screen = pyagme.display.set_mode(size)
        #修改窗口大小
        elif event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size , RESIZABLE)
        elif event.type == KEYUP:
            position = [0, 0]
        #检测右上角×
        elif event.type == QUIT:
            running = False
    #图像移动
    man_rect = man_rect.move(position)
    #边界检测
    if man_rect.left < 0 or man_rect.right > width or man_rect.top < 0 or man_rect.bottom > height:
        position = [0, 0]

    screen.fill((bg))
    screen.blit(man, man_rect)
    pygame.display.flip()