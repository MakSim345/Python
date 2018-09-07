# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random


debug=False
ur_guess=""
secret_number=0
low_range=0
high_range=100
games=0
guess_count=0



# helper function to start and restart the game
def new_game(low, high):
    # initialize global variables used in your code here
    global secret_number
    global games
    global guess_count
    global low_range
    global high_range
    low_range=low_range
    high_range=high
    games+=1
  


    secret_number=random.randrange(low, high)
    n=0
    while 2 ** n < (high_range - low_range + 1):
        n+=1
    guess_count = n
    if debug:
        print
        print "Debug:  Game Count =", games
        print "Debug:  guess_count=", guess_count
    print "Starting game "+ str(games) + " with Range " + str(low) + "-" + str(high)
    return
        
        

# define event handlers for control panel
def range100():
    new_game(0, 100)

def range1000():
    new_game(0, 1000)
    


    
def input_guess(guess):
    # main game logic goes here 
    global ur_guess
    global guess_count
    guess_count=guess_count -1
    if debug:
        print "Debug:  Number of guesses is now", guess_count
        print "Debug:  Secret Number is", secret_number
    """
    Test that the input is a number
    """
    try:
        test=float(guess)
        if float(int(test)) == test:
            ur_guess = int(test)
        else:
            ur_guess = test
    except:
        print "Numbers only please."
        new_game(low_range, high_range)
        return
    
    print "Guess was", ur_guess
        
    if ur_guess == secret_number:
        print "Correct!"
        print "New Game!"
        new_game(low_range, high_range)
        return
    if guess_count > 0:
        if ur_guess < secret_number:
            print "Higher"
            print "You have "+ str(guess_count) + " guesses left."
            
        else:
            print "Lower"
            print "You have "+ str(guess_count) + " guesses left."
    if guess_count < 1:
        print "Your out of guesses.  Game Over! The number was", secret_number
        new_game(low_range, high_range)
    print
 
   
# create frame
frame=simplegui.create_frame("Guessing Game",300,300)

# register event handlers for control elements and start frame
inp_guess = frame.add_input('Your Guess', input_guess, 50)
button_range_100 = frame.add_button('Range: 0 - 100', range100)
button_range_1000 = frame.add_button('Range: 0 - 1000', range1000)
frame.start()
# call new_game 
new_game(low_range, high_range)


# always remember to check your completed program against the grading rubric


- great job! 
especially I like that you are using "try-except" methods already and using counter for total games.

line 
print "You have "+ str(guess_count) + " guesses left."
is called in both cases of the if-else, so it is possible to move it outside of if-else structure.