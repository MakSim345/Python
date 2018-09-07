x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
 
import pygame
pygame.init()
screen = pygame.display.set_mode((100,100))
 
# wait for a while to show the window.
import time
time.sleep(2)

