# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui    #import grafical module
import random       #import random module

game_range = 100        #The game range
allowed_guesses = 7     #The number of guesses
remaining_guesses = 7   #The number of remaining guesses
player_guess = 0        #The number a player choose
secret_number = 0       #The secret number


# helper function to start and restart the game
def new_game():
    
    # initialize global variables used in your code here
    global game_range, allowed_guesses, remaining_guesses
    global secret_number
    
    #Assigne allowed guesses based on game_range 
    if (game_range == 100):
        #Assigne remaining guesses and allowed guesses to 7
        remaining_guesses = allowed_guesses = 7
    else:
        #Assigne remaining guesses and allowed guesses to 10
        remaining_guesses = allowed_guesses = 10
  
    #Assigne e random value for the secret value
    secret_number = random.randrange(0, game_range)
    
    print "New game. Range is from 0 to", game_range
    print "Number of remaining guesses is", remaining_guesses


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global game_range
    
    game_range = 100    #Assigne game range to 100
    
    print ""            #Break line
    
    new_game()          #Start new game

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global game_range
    
    game_range = 1000   #Assigne game range to 1000
    
    print ""            #Break line
    
    new_game()          #Start new game
    
def input_guess(guess):
    # main game logic goes here
    global player_guess, remaining_guesses, secret_number
    
    #Convert string of player guess to integer
    player_guess = int(guess)     
        
    remaining_guesses -= 1      #Decrease remaining guesses 
      
    print ""                    #Break line
    
    print "Guess was", player_guess
    print "Number of remaining guesses is", remaining_guesses

    
    #Check if player guesses correct
    if (player_guess == secret_number):
        print "Correct!"
        print ""
        new_game()
    #Check if the guess is lower than secret number or not
    elif (player_guess < int(secret_number)):
        print "Higher!"
    else:
        print "Lower!"
    
    #If no more remaining guesses then print a message
    #And restart the game
    if (remaining_guesses == 0):
        print ""
        print "No more guesses! Try play Again"
        print ""
        
        new_game()  #Start the game
    

    
# create frame
frame = simplegui.create_frame("frame name", 200, 200)
#Set frame backgournd color
frame.set_canvas_background('Black')

# register event handlers for control elements and start frame
#Button for range [0, 100)
frame.add_button("Range is [0, 100)", range100, 125)
#Button for range [0, 1000)
frame.add_button("Range is [0, 1000)", range1000, 125)
#Text input field
frame.add_input("Enter a guess", input_guess, 120)
#Start the frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric


- doublication of 
print "Number of remaining guesses is", remaining_guesses
may be placed to one separate function.

- in line 
frame.add_button("Range is [0, 100)", range100, 125)
remind that 125px is too small for button caption to be placed in one line. 