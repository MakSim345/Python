# implementation of card game - Memory

import simplegui
import random
numbers= [1,5,7,4,4,6,7,8,1,8,3,2,2,6,3,5]
A=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
E = [False,False,False,False, False,False,False,False,False,False,False,False,False,False,False,False] 
state = 0
last = 0
ancient = 0

# helper function to initialize globals
def new_game():
    global A, numbers, E
    random.shuffle(numbers)
    A = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    E = [False,False,False,False, False,False,False,False,False,False,False,False,False,False,False,False] 
    frame.set_draw_handler(draw)
     
# define event handlers
def mouseclick(pos):
    global A,state, last, ancient,E
    if (pos[0] >= 0) and (pos[0]<50):
        ##################################
        if state == 0:
            E[0] = True
        
        
        ##################################        
    elif (pos[0] >= 50) and (pos[0] < 100):
         if state==0:
                E[1] = True
    elif (pos[0] >= 100) and (pos[0] < 150):
         if state == 0:
                E[2] = True
            
 
    elif (pos[0] >= 150) and (pos[0] < 200):
     A[3] = str(numbers[3])
     E[3] = True   
    elif (pos[0] >= 200) and (pos[0] < 250):
     A[4] = str(numbers[4])
     E[4] = True
    elif (pos[0] >= 250) and (pos[0] < 300):
     A[5] = str(numbers[5]) 
     E[5] = True
    elif (pos[0] >= 300) and (pos[0] < 350):
     A[6] = str(numbers[6])
     E[6] = True
    elif (pos[0] >= 350) and (pos[0] < 400):
     A[7] = str(numbers[7])
     E[7] = True
    elif (pos[0] >= 400) and (pos[0] < 450):
     A[8] = str(numbers[8])
     E[8] = True
    elif (pos[0] >= 450) and (pos[0] < 500):
     A[9] = str(numbers[9])   
     E[9] = True
    elif (pos[0] >= 500) and (pos[0] < 550):
     A[10] = str(numbers[10]) 
     E[10] = True
    elif (pos[0] >= 550) and (pos[0] < 600):
     A[11] = str(numbers[11])
     E[11] = True
    elif (pos[0] >= 600) and (pos[0] < 650):
     A[12] = str(numbers[12])   
     E[12] = True
    elif (pos[0] >= 650) and (pos[0] < 700):
     A[13] = str(numbers[13])
     E[13] = True
    elif (pos[0] >= 700) and (pos[0] < 750):
     A[14] = str(numbers[14])
     E[14] = True
    elif (pos[0] >= 750) and (pos[0] < 800):
     A[15] = str(numbers[15])
     E[15] = True
    print E
    print state

        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global A,E
    for n in range(0,16):
     canvas.draw_line((50*(0.5+n),5), (50*(0.5+n),95), 45, 'Blue')
    for n in range(0,16):
     if E[n] == True:
        A[n] = str(numbers[n])        
     else:
             A[n] =" "
     canvas.draw_text(A[n], (50*(0.4+n), 63), 30, 'Red')
    
        
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



# Always remember to review the grading rubric