import sys
import pygame
from pygame.locals import *
 
def init_window():
    pygame.init()
    window = pygame.display.set_mode((550, 480))
    pygame.display.set_caption('My own little world')
 
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
    init_window()
    action()
 
if __name__ == '__main__': 
    
    main()

