# implementation of card game - Memory
'''
Well done. 
Unfortunately you commit an app with major bug- app haven't start at all, please be more careful with pushing your work to central repository. 
The game haven't react to mouse click, so I couldn't test every feature, but some are working fine.
Here the version I was used:
http://www.codeskulptor.org/#user38_JqKGEh0Vs8djQEd_0.py
'''

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

card_pos = range(16)
card_value = range(8)
deck = range(8) + range(8)
exposed = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False,]
state = 0
click_1 = 0
click_2 = 0
count = 0

#Helper function to initialize globals
def new_game():
    global exposed, state, click_1, click_2
    random.shuffle(deck)
    exposed = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False,]
    state = 0
    click_1 = 0
    click_2 = 0
    
# function to find card_index of a card
def card_index(card):
    for card in card_pos:
        return card_pos.index(card)    
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, click_1, click_2, count
    clicked_card = (pos[0] // 50)
        
    if state == 0:
        exposed[clicked_card] == True
        click_1 = clicked_card
        state += 1
    elif state == 1:
        if click_1 == click_2:
            pass
        else:
            exposed[clicked_card] == True
            click_2 = clicked_card
            state += 1 
    else:
        if deck[click_1] == deck[click_2]:
            exposed[click_1] == True
            exposed[click_2] == True
                        
        else:
            exposed[click_1] = False
            exposed[click_2] = False
        exposed[clicked_card] = True    
                     
        state = 1
    count += 1
     
            
        
        
    
    
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, card_pos, deck
    
    for i in card_pos:
        canvas.draw_line(((49 + 50 * i), 0), ((49 + 50 * i), 99), 6, 'Black')
        a = card_pos.index(i)
        text_pos = [(10 + a * 50), 65]
        text = str(deck[a])
        if exposed[a] == True:
            canvas.draw_text(text, text_pos, 40, "Black")                
        else:
            canvas.draw_text(text, text_pos, 40, "Red")
        #endif
    #endfor        
        
            
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background("Green")
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " +str(count))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric