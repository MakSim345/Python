#!/usr/bin/env python

#############################################################################
##
##
#############################################################################

import math
import os, sys
import traceback
import pygame

number = 5

def TimeTest001():
    # time.clock() gives wallclock seconds accurate to at least 1 millisecond
    # it updates every millisecond, but only works with windows
    # time.time() is more portable, but has quantization errors
    # since it only updates updates 18.2 times per second
    import time
    print "\nTiming a 1 million loop 'for loop' ..."
    start = time.clock()
    for x in range(1000000):
        y = 100*x - 99 # do something
    end = time.clock()
    print 'start', start
    print 'end', end
    print "Time elapsed = ", end - start, "seconds"
    """
    result -->
    Timing a 1 million loop 'for loop' ...
    Time elapsed = 0.471708415107 seconds
    """
def TimeTest002():
    import time
    import sys
    print sys.getcheckinterval()
    for i in range (100):
         # now = time.time()
         now = time.clock()
         # b = time.__doc__()
         print i, " - ", now
    print 'STOP'

def TimeTest003():
    import time
    import sys
    import arrays

    for i in range (10):
         now = time.clock()
         # b = time.__doc__()
         print i, " - ", now, "QT: ", m_ms.elapsed()

    print 'STOP'

def SaveStatus(data_to_save):
    import pickle, time, sys
    # mydata = ("abc", 12, [1, 2, 3])
    output_file = open("mydata.dat", "w")
    p = pickle.Pickler(output_file)
    p.dump(data_to_save)
    output_file.close()

def ReadStatus():
    import pickle, time, sys
    output_file = open("mydata.dat", "w")
    p = pickle.Pickler(output_file)
    p.get(data_to_save)
    output_file.close()

def MyArray():
    a = [676.7, 353, 433, 14, 14.565]
    # a.sort()
    # print a
    return a
    
def MyTuple():
    a = [MyArray(), someInt(), someFloat()]
    # a = [66.6, 333, 333, 'Damn world', 1, 1234.5]
    # a.sort()
    for i in a:
        print i
    #return a
    
    
def dictTest():
    DeliveryStarted = 0
    DeliveryStopped = 1
    FGTotalFlowChanged = 2
    AgentTypeChanged = 3
    OxygenPercentageChanged = 4
    AirPercentageChanged = 5
    N2OPercentageChanged = 6
    AgentPercentageChanged = 7
    DummyAlarm = 8
    m_Array = {}  
    
    m_Array[DeliveryStarted]        = MyArray()
    m_Array[DeliveryStopped]        ="DeliveryStopped" 
    m_Array[FGTotalFlowChanged]     ="FGTotalFlowChanged" 
    m_Array[AgentTypeChanged]       ="AgentTypeChanged" 
    m_Array[OxygenPercentageChanged]="OxygenPercentageChanged" 
    m_Array[AirPercentageChanged]   ="AirPercentageChanged" 
    m_Array[N2OPercentageChanged]   ="N2OPercentageChanged" 
    m_Array[AgentPercentageChanged] ="AgentPercentageChanged" 
    m_Array[DummyAlarm]            ="DummyAlarm"
    
    if DeliveryStarted in m_Array:
        m_Array[0]

    for key, value in m_Array.iteritems():
        print key, value    


class MyClass():
    def __init__(self):
        self.a = 100
        self.__b = 200
        
    def dump(self):    
        print "My value a = ", self.a

    def dump_b(self):
        '''test private member'''
        print "My value __b = ", self.__b

class XAKEP():
    def __init__(self):
        self.WIN_WIDTH = 800
        self.WIN_HEIGHT = 640
        # self.DISPLAY = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.DISPLAY = (800, 640)
        self.BACKGROUND_COLOR = "#004400"
        

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.DISPLAY)
        pygame.display.set_caption("][akep")
        #bg = pygame.Surface(self.WIN_WIDTH, self.WIN_HEIGHT)
        bg = pygame.Surface((self.DISPLAY))
        bg.fill(pygame.Color(self.BACKGROUND_COLOR))
        
        pygame.draw.line(bg, (10,100,100),(10,200),(20,300),2)
        
        while 1:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    raise SystemExit ,"QUIT"
                #endif
            screen.blit(bg, (0,0))    
            pygame.display.update()
            #endfor        
         #endwhile
            
if __name__ == "__main__":    

    print "Main program start."
    print ""
    print "Python version: "
    print sys.version
    print "----------------------\n"

    try:
        sm = XAKEP()
        sm.run()        
        # TimeTest001()
    except NotImplementedError, e:
        print "1. Error occures:",  e
    except:
        print "2. Error occures: unknown"
        traceback.print_exc()    


    print "Main program ends"

