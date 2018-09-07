#!/usr/bin/env python
# -*- coding: utf8 -*-
# -*-coding:cp1251 -*-

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback

import pygame

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

def screen_setup():
    '''
    '''

def main_app():
    # This sets the margin between each cell
    margin = 1
    
    # This sets the width and height of each grid location
    width = 5
    height = 5
    cell_number = 80
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # Create a 2 dimensional array. A two dimesional
    # array is simply a list of lists.
    grid = []
    for row in range(cell_number):
        # Add an empty array that will hold each cellin this row
        grid.append([])
        for column in range(cell_number):
            grid[row].append(0) # Append a cell
        #endfor
    #endfor    
        
    # Set row 1, cell 5 to one. (Remember rows and
    # column numbers start at zero.)
    grid[5][5] = 1
    
    # Set the height and width of the screen
    size = [500, 500]
    screen=pygame.display.set_mode(size)

    # -------- Main Program Loop -----------
    while done == False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            #endif                    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit ,"QUIT"
            #endif                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                # Sete t hat location to zero
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
                # Set the screen background
                screen.fill(black)
            #endif
             
        # Draw the grid
        for row in range(cell_number):
            for column in range(cell_number):
                color = white
                if grid[row][column] == 1:
                    color = green
                pygame.draw.rect(screen, color,
                    [(margin+width)*column+margin,
                    (margin+height)*row+margin, width, height])
                #endif    
            #endfor    
        #endfor    
                
        # Limit to 20 frames per second
        clock.tick(20)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

if __name__ == "__main__":    

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"
    
    # Initialize pygame
    pygame.init()
    # Set title of screen
    pygame.display.set_caption("Array Backed Grid")
    
    try:
        screen_setup()
        main_app()
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    print "Main program ends"
