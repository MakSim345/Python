# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
import random
import math

secret_number = 0
current_range = 100 # by default is 100
remaining_gueses = 7 # by default is for 100

# helper function to start and restart the game
def new_game():
    global secret_number
    
    # refresh number of remainin guesses for new game
    if (current_range == 100):
        range100()
    else:
        range1000
    #endif
    
    secret_number = random.randrange(0, current_range)
    #print "new secret number = ", str(secret_number)
    print "\nNew game. Range is from 0 to " + str(current_range)
    print_out_remainig_guesses()
    
def print_out_remainig_guesses():
    print "Number of remainin guesses is " + str(remaining_gueses)
    
def set_range(new_range):
    global current_range 
    current_range = new_range
    
def set_rem_guesses(new_rem_guess):
    global remaining_gueses
    remaining_gueses = new_rem_guess

def press_range100():
    ''' click handler for button 100'''
    range100()
    new_game()

def press_range1000():
    ''' click handler for button 1000'''
    range1000()
    new_game()
    
def range100():
    ''' set rnd limit up to 100 and guess limit 10'''
    set_range(100)
    set_rem_guesses(7)
   
def range1000():
    ''' set rnd limit up to 1000 and guess limit 10'''
    set_range(1000) 
    set_rem_guesses(10)
    
def input_guess(guess):
    # main game logic goes here	
    print "\nGuess was", guess
    int_guess = int(guess)
    set_rem_guesses(remaining_gueses - 1)
    print_out_remainig_guesses()
    
    if (int_guess == secret_number):
        print "Correct!"
        new_game()
    else:
        if (int_guess > secret_number):
            print "Lower!"
        elif(int_guess < secret_number):
            print "Higher!"
        #endif
        
        if (remaining_gueses <= 0):
            print "You have exceeded the maximum number of guesses. Game over!"
            new_game()
        #endif    
    #endif
#end_def

# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements
frame.add_button("Range is  [0, 100)", press_range100, 200)
frame.add_button("Range is  [0, 1000)", press_range1000, 200)
frame.add_input('Enter a guess:', input_guess, 200)

# and start frame
frame.start()

# call new_game 
new_game()

