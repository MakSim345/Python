# implementation of card game - Memory

import simplegui
import random

'''
Great job. Colors and "Gamo over" are best
'''

# helper function to initialize globals

card_matched = []
deck = []
state = 0
card1_num = card2_num = -1    # -1  for not selected
game_over = False
turns = -1
matched_pair = False
overx = 0


def new_game():
    global deck, card_matched
    global state,card1_num, card2_num
    global overx, game_over, turns
    
    deck = range(8)+range(8)
    random.shuffle(deck)
    card_matched = 16*[False]
    card1_num = card2_num = -1  
    state = 0
    turns = -1
    turnsplus1()
    overx = 0
    game_over = False
    matched_pair = False
    print deck
    
def matched_count():
    global card_matched
    count = 0
    for visible in card_matched:
        if visible:  count += 1
    return count

     
# define event handlers
def mouseclick(pos):
# Process valid card selections, test for game over
#
# When selection card1 and card2,
#  they may not be a previously matched card.
# When selecting card2,
#  it may not be the same as card1.
# After selecting card2, check for match and game over.

    global state,  card1_num, card2_num
    global matched_pair, game_over
    
    card_num = pos[0]/50
    
    if card_matched[card_num]:  #ignore click on visible card
        return
    
    if state == 0:
        state = 1
        card1_num = card_num
        card2_num = -1   

    elif state == 1:
        card2_num = card_num
        if card2_num != card1_num:  # ignore click card twice
            state = 2
            turnsplus1()
            matched_pair = match_cards(card1_num, card2_num)
            if matched_pair: print "Match",(card1_num,card2_num)
            if matched_count() == 16:
                game_over = True
    else:
        card1_num = card_num
        card2_num = -1
        state = 1

    if game_over: print "Gameover"
      
# Update and display turn count   
def turnsplus1():
    global turns
    turns += 1
    label.set_text("Turns = " +str(turns))
    
# Do cards 1 and 2 match?
def match_cards(card1_num, card2_num):
    global deck, card_matched
    match = False
    if deck[card1_num] == deck[card2_num]:
        card_matched[card1_num] = card_matched[card2_num] = True
        match = True
    return match
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global game_over, overx
    draw_all_cards(canvas)
    if game_over:
        canvas.draw_text("Game Over", (overx+200,80),24,"Green")
        overx = (overx+3)%200

# Draw all cards as face up or down
def draw_all_cards(canvas):
    for i in range(16):
        draw_card(canvas, i)

# Draw a single card
def draw_card(canvas, i):
# Matched cards and current selection (card1, card2) shown face up
# Other cards shown face down

    global card_matched,card1_num, card2_num
    
    if card_matched[i] :
        # Draw matched cards face up
        draw_rect(canvas, [50*i,100], [50,100], 2, "Blue", "Red")
        canvas.draw_text(str(deck[i]), (50*i+12,65), 36, 'Black', 'sans-serif') 
    elif card_matched[i] or i == card1_num or i == card2_num:
        # Draw selected cards face up
        draw_rect(canvas, [50*i,100], [50,100], 2, "Blue", "Yellow")
        canvas.draw_text(str(deck[i]), (50*i+12,65), 36, 'Black', 'sans-serif') 
    else:
        #Draw remaining cards face down
        draw_rect(canvas, [50*i,100], [50,100], 2, "Blue", "Green")
      
    
def draw_rect(canvas,pt,size, linewidth,linecolor,fillcolor):
    (x,y) = pt
    (sx,sy) = size
    canvas.draw_polygon( \
        ((x, y), (x, y-sy), (x+sx, y-sy),(x+sx, y)), \
        linewidth, linecolor, fillcolor)


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