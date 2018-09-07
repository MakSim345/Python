import sys
import pygame
from pygame import *


#From: https://www.youtube.com/watch?v=AaGK-fj-BAM

def setup():
    DISPLAY = (600, 600)
    BACKGROUND_COLOR = "#002400"
    pygame.init()
    window = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption('SNAKE - code challenge')
    bg = Surface((DISPLAY))
    bg.fill(Color(51))
    window.blit(bg, (0,0)) 
 
def input(events):
    for event in events:
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
        else:
            pass
 
def action():
    while 1:
        input(pygame.event.get())
 
def main():
    setup()
    action()
 


 
if __name__ == '__main__':     
    main()

