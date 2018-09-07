import os
import pygame
import time
import random
import serial

SERIAL_PORT = 'COM4'
SERIAL_SPEED = 38400

class pyscope :
    screen = None;
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        self.WIN_WIDTH = 800
        self.WIN_HEIGHT = 640
        # self.DISPLAY = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.DISPLAY = (800, 640)
        self.BACKGROUND_COLOR = "#004400"

        
        # size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        # print "Framebuffer size: %d x %d" % (size[0], size[1])
        # self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        
        self.screen = pygame.display.set_mode(self.DISPLAY)
        pygame.display.set_caption("Super OSC")
        #bg = pygame.Surface(self.WIN_WIDTH, self.WIN_HEIGHT)
        bg = pygame.Surface((self.DISPLAY))

        # Clear the screen to start
        self.screen.fill((0, 0, 0))        
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."
    
    def drawGraticule(self):
        "Renders an empty graticule"
        # The graticule is divided into 10 columns x 8 rows
        # Each cell is 50x40 pixels large, with 5 subdivisions per
        # cell, meaning 10x8 pixels each.  Subdivision lines are
        # displayed on the central X and Y axis
        # Active area = 10,30 to 510,350 (500x320 pixels)
        borderColor = (255, 255, 255)
        lineColor = (64, 64, 64)
        subDividerColor = (128, 128, 128)
        # Outer border: 2 pixels wide
        pygame.draw.rect(self.screen, borderColor, (8,28,504,324), 2)
        # Horizontal lines (40 pixels apart)
        for i in range(0, 7):
            y = 70+i*40
            pygame.draw.line(self.screen, lineColor, (10, y), (510, y))
        # Vertical lines (50 pixels apart)
        for i in range(0, 9):
            x = 60+i*50
            pygame.draw.line(self.screen, lineColor, (x, 30), (x, 350))
        # Vertical sub-divisions (8 pixels apart)
        for i in range(1, 40):
            y = 30+i*8
            pygame.draw.line(self.screen, subDividerColor, (258, y), (262, y))
        # Horizontal sub-divisions (10 pixels apart)
        for i in range(1, 50):
            x = 10+i*10
            pygame.draw.line(self.screen, subDividerColor, (x, 188), (x, 192))

    def test(self):
        "Test method to make sure the display is configured correctly"
        adcColor = (0, 255, 0)  # Yellow
        self.drawGraticule()
        # Render the Adafruit logo at 10,360
        # logo = pygame.image.load('adafruit_logo.gif').convert()
        #self.screen.blit(logo, (10, 335))
        
        # Get a font and use it render some text on a Surface.
        font = pygame.font.Font(None, 30)
        text_surface = font.render('pyScope (%s)' % "0.1", 
            True, (255, 255, 255))  # White text
        # Blit the text at 10, 0
        self.screen.blit(text_surface, (10, 0))
        # Render some text with a background color
        text_surface = font.render('Channel 0',
            True, (0, 0, 0), (255, 255, 0)) # Black text with yellow BG
        # Blit the text
        self.screen.blit(text_surface, (540, 30))
        # Update the display
        pygame.display.update()
        # Random adc data
        
        ser = serial.Serial(SERIAL_PORT, SERIAL_SPEED)        
        
        while (1):            
            self.screen.fill((0, 0, 0))
            self.drawGraticule()
            yLast = 260
            y = 0
            print "new round\n"
            for x in range(10, 509):         
                y = random.randrange(30, 350, 2) # Even number from 30 to 350
                #s = ser.readline().strip()                
                #if str.isalnum(s):
                #    y = int(s)
                pygame.draw.line(self.screen, adcColor, (x, yLast), (x+1, y))
                yLast = y                
                pygame.display.update()
                print x, yLast


def get_data_from_com():
    print "hello"
    ser = serial.Serial(SERIAL_PORT, SERIAL_SPEED)
    while (1):    
    # for i in range(0, 400):
        # s = ser.read()
        s = ser.readline().strip()
        # print str(i), " - ", s, "\n"
        if str.isalnum(s):
            # self.drawdata(float(s))
            print_graph(s)
        #endif
    #end_for
    return 
#end_def

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    # Create an instance of the PyScope class
    scope = pyscope()
    scope.test()
    # Wait 10 seconds
    # time.sleep(5)
    print ""    
    print "Main program end."
