# Mini-project #6 - Blackjack

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simpleguics2pygame
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


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
        self.cards=[]

    def __str__(self):
        if len(self.cards) > 0:
            string = ''
            for card in self.cards:
                string += str(card) + ' '
            return string
        else:
            return 'empty'
        
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        has_ace = False
        if len(self.cards) > 0:
            for card in self.cards:
                if (card.get_rank() == 'A') :
                    has_ace = True
                value += VALUES[card.get_rank()]
            if not has_ace:
                return value
            else:
                if value + 10 <= 21:
                    return value + 10
                else:
                    return value
        else:
            return 0
        
  
    def draw(self, canvas, pos):
        #pass   # draw a hand on the canvas, use the draw method for cards
        i = 0
        for card in self.cards:
            if i < 5:
                card.draw(canvas,pos)
                i += 1
                pos[0] += 90
 
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_cards=[]
        self.played_cards=[]
        for suit in SUITS:
            for rank in RANKS:
                self.deck_cards.append(Card(suit,rank))          

    def shuffle(self):
        if len(self.played_cards) > 0:
            self.deck_cards.extend(self.played_cards )
        random.shuffle(self.deck_cards)

    def deal_card(self):
        #THandling if all cards are already played
        if len(self.deck_cards) == 0:
            self.deck_cards.extend(self.played_cards)
        card = self.deck_cards.pop(0)
        self.played_cards.append(card)
        return card 
    
    def __str__(self):
        if len(self.deck_cards) > 0:
            string = ''
            for card in self.deck_cards:
                string += str(card) + ' '
            return string
        else:
            return 'empty'

#define event handlers for 
deck = Deck()
dealer_hand = Hand()
player_hand = Hand()
def deal():
    global outcome, in_play, deck, score
    global dealer_hand, player_hand
    
    if not in_play:
        deck.shuffle();
        
        dealer_hand = Hand()
        player_hand = Hand()
    
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
    
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        outcome = "Hit or Stand?"
        in_play = True
    else:
        outcome = 'You lose. New Deal?'
        score -= 1
        in_play = False

def hit():
    global in_play, player_hand, score,deck, outcome
 
    # if the hand is in play, hit the player
    if in_play:
        if player_hand.get_value() < 21:
            player_hand.add_card(deck.deal_card())
   
        print('Deck of Player:')
        print(str(player_hand))
        print(str(player_hand.get_value()))   
        if player_hand.get_value() > 21:
            outcome = 'You went busted.'
            in_play = False
            score -= 1
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, dealer_hand, player_hand, outcome, score
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            
        if dealer_hand.get_value() > 21:
            outcome = 'You win. New Deal?'
            score += 1
        elif dealer_hand.get_value() >= player_hand.get_value():
            outcome = 'You lose. New Deal?'
            score -= 1
        else:
            outcome = 'You win.New Deal?'
            score += 1

        in_play = False

# draw handler    
def draw(canvas):
    global score, outcome
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    
    #canvas.draw_text(text, point, font_size, font_color)
    canvas.draw_text('Black Jack', (50,60), 50, 'Blue')
    
    canvas.draw_text('Dealer:', (50,120), 40, 'Black')

        
    canvas.draw_text('Player:', (50,280), 40, 'Black')
    canvas.draw_text(str(player_hand.get_value()), (200,280), 40, 'Black')
    
    canvas.draw_text(str(outcome), (50,450), 40, 'Grey')
    
    canvas.draw_text('Score: ' + str(score), (50,550), 40, 'Orange')
    
   
    player_hand.draw(canvas,[50,290])
    dealer_hand.draw(canvas,[50,130])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (86,178), CARD_BACK_SIZE)
    else:
        canvas.draw_text(str(dealer_hand.get_value()), (200,120), 40, 'Black')
   

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
