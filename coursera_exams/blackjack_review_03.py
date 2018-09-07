
'''
Well done!
Few comments:
- it would be easyer to see current card range in digit form as well. I hate to calculate grapic images every time in order to see why "dealer wins"...
- Why it looks like only "dealer" is playing? "Dealer wins" and "dealer is busted"? Waht about me, in form: "you win, you loose"?
'''

# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (37, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False 
outcome = "" 
score = 0
wins = 0
losts = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
start_pos_player_cards = [50, 420]
gap = 10
start_pos_dealer_cards = [50, 220]
end_game = False 

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
           

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:    
    def __init__(self):
        self.cards = [] 

    def __str__(self):
        card_in_hand = ''     
        for c in self.cards:
            card_in_hand += str(c) + ' '        
        return 'Hand contains ' + card_in_hand

    def add_card(self, card):
        self.cards.append(card)        
        return self

    def get_value(self):      
        value_of_hand = 0
        ranks_of_cards_in_hand = ''
        
        for card in self.cards:         
            value_of_hand += VALUES[card.rank]       
            ranks_of_cards_in_hand += card.rank
            
        
        if not ('A' in ranks_of_cards_in_hand):
            return value_of_hand
        else: 
            if value_of_hand + 10 <= 21:
                return value_of_hand + 10
            else:
                return value_of_hand        
                
    def draw(self, canvas, pos):
        global start_pos_player_cards, gap
        self.draw(canvas,pos) 

# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        
        self.cards = [] 
        
        for cr in range(len(RANKS)): 
            for cs in range(len(SUITS)):          
                c = Card(SUITS[cs], RANKS[cr])
                self.cards.append(c)                                         

    def shuffle(self):      
        random.shuffle(self.cards)
        
    def deal_card(self):  
        dealt_card = self.cards[0]
        self.cards.remove(dealt_card)        
        return dealt_card
    
    def __str__(self):     
        cards_in_deck = ''
        
        for c in self.cards:
            cards_in_deck += str(c) + ' '        
        return 'Deck contains ' + cards_in_deck

# define event handlers for buttons
 
def deal():
    global outcome, in_play, score, wins, losts, end_game
    global card_deck, dealer_hand, player_hand
    
    if in_play: 
        score -= 1
        losts += 1
        outcome = 'Player loses! New deal?'
        in_play = False 
        end_game = True  
    else:
        card_deck = Deck() 
        player_hand = Hand()
        dealer_hand = Hand()
        card_deck.shuffle() 
        end_game = False
        
        c1 = card_deck.deal_card()
        player_hand.add_card(c1) 
           
        c2 = card_deck.deal_card()
        player_hand.add_card(c2)
            
        c3 = card_deck.deal_card() 
        dealer_hand.add_card(c3)         
        c4 = card_deck.deal_card() 
        dealer_hand.add_card(c4)      
        outcome = 'Hit or Stand?'
        in_play = True 
      
   
def hit():
    global player_hand, card_deck, score, outcome, in_play, losts, wins, end_game
    
    if not end_game: 
        
        if player_hand.get_value() <= 21:
            c = card_deck.deal_card() 
            player_hand.add_card(c)           
            outcome = 'Hit or Stand?'            
            if player_hand.get_value() > 21:
                outcome = "You have busted! New deal?"             
                score -= 1             
                losts += 1
                in_play = False 
                end_game = True
              
     
def stand():
    global player_hand, dealer_hand, score, outcome, in_play, wins, losts, end_game
   
    in_play = False 
    
    if not end_game:
       
        if player_hand.get_value() > 21:       
            outcome = "You have busted! New deal?"                                   
            end_game = True
           
        else:
            while dealer_hand.get_value() < 17:
                c = card_deck.deal_card() 
                dealer_hand.add_card(c)            
               
                
            if  dealer_hand.get_value() > 21:                                                  
                outcome = 'Dealer is busted! New deal?'
                score += 1
                wins += 1    

            else:
                if player_hand.get_value() > dealer_hand.get_value():                
                    outcome = 'Player wins! New deal?'
                    score += 1
                    wins += 1                   
                else:                    
                    outcome = 'Dealer wins! New deal?'
                    score -= 1               
                    losts += 1
        end_game = True  
              
def reset():
    global player_hand, dealer_hand, score, outcome, in_play, wins, losts, end_game
    card_deck = Deck() 
    player_hand = Hand() 
    dealer_hand = Hand() 
    card_deck.shuffle()
    score = 0
    wins = 0
    losts = 0
    outcome = 'New game.'
    in_play = False
    end_game = False
    deal()
            
# Draw handler    
def draw(canvas):
    global start_pos_player_cards, start_pos_dealer_cards, gap
    global player_hand, dealer_hand, score, outcome, in_play, wins,losts
    canvas.draw_text("Blackjack",[50, 100], 35, "Cyan")
    canvas.draw_text("Dealer",[50, 200], 35, "Black")       
    if in_play: 
        c = dealer_hand.cards[0]
        pos0 = [start_pos_dealer_cards[0], start_pos_dealer_cards[1]]
        dealer_hand.cards[0].draw(canvas, pos0)

        pos1 = [start_pos_dealer_cards[0] + gap + CARD_SIZE[0], start_pos_dealer_cards[1]] 
        pos12 = [pos1[0] + CARD_BACK_CENTER[0], pos1[1] + CARD_BACK_CENTER[1]]
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, pos12,CARD_BACK_SIZE)
    else:       
        for i in range(len(dealer_hand.cards)):       
            c = dealer_hand.cards[i]
            pos = [start_pos_dealer_cards[0] + (gap + CARD_SIZE[0])*i, start_pos_dealer_cards[1]]
            dealer_hand.cards[i].draw(canvas, pos)                  
    
    # Player's area 
    canvas.draw_text("Player",[50, 400], 35, "Black")
    canvas.draw_text("Score:",[350, 100], 30, "Black")
    canvas.draw_text(str(score),[450, 100], 30, "White")     
    canvas.draw_text(outcome, [250, 400], 30, "Black")  
    
# player's cards
    if len(player_hand.cards) > 0:
        for i in range(len(player_hand.cards)):
            if i <=5:
                c = player_hand.cards[i]
                pos = [start_pos_player_cards[0]+ (gap + CARD_SIZE[0])*i, start_pos_player_cards[1]]
                player_hand.cards[i].draw(canvas, pos)
                
# initialization frame               
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
label = frame.add_label("BLACKJACK")
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
label = frame.add_label(" ")
frame.add_button("Start new game", reset, 200)
frame.set_draw_handler(draw)
player_hand = Hand()
dealer_hand = Hand()

# get things rolling
deal()
frame.start()
