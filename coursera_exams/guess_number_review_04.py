# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

#print math.ceil(math.log(100, 2))

upper_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    
    global secret_number 
    global upper_range
    global count
    print "New game. Range is from 0 to ", upper_range
    print "Number of remaining guesses is ", math.ceil(math.log(upper_range, 2))    
    print "\n"
    secret_number = random.randint(0, upper_range)
    count = math.ceil(math.log(upper_range, 2))

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global upper_range
    upper_range = 100
    new_game()    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global upper_range
    upper_range = 1000 
    new_game()
       

def input_guess(guess):
    # main game logic goes here
    
    global secret_number
    global count
    global upper_range
    
    if count < 1 :
        print "Times up! No more chances!\n "
        #new_game()
        #count = count + 1
    else : 
        count = count - 1
        guessint = int(guess)
        print "Guess was ", guessint
        print "Number of remaining guesses: ", count
        
        if guessint > secret_number :
            print "Lower!\n"
        elif guessint < secret_number :
            print "Higher!\n"
        else : 
            print "Correct!\n"
            new_game()
           # count = count + 1  
   
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_input('input guess', input_guess, 100)
frame.add_button('range 1-100', range100, 100)
frame.add_button('range 1-1000', range1000, 100)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric


doublicates:
math.ceil(math.log(upper_range, 2)) 
I would first calculate: 
count = math.ceil(math.log(upper_range, 2))
and then print "count" out in "Number of remaining guesses is", instead of recalculation.

in function input_guess(guess):
there is declaration of "upper_range", but no usage.