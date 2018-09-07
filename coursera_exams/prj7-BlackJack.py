
# import simpleguitk as simplegui
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

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
outcome = ""
player_points = ""
current = ""
score = 0
dealer = []
player = []
deck = []

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
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, x, y, faceDown = True):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [x + CARD_CENTER[0], y + CARD_CENTER[1]], CARD_SIZE)
        
        if faceDown == True:
            card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [x + CARD_BACK_CENTER[0], y + CARD_BACK_CENTER[1]], CARD_SIZE)
        #endif    
            
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return ','.join([card.get_suit() + card.get_rank() for card in self.hand])
    
    def add_card(self, card):
        '''add a card object to a hand'''
        self.hand.append(card)

    def get_value(self):
        '''
        count aces as 1, if the hand has an ace, 
        then add 10 to hand value if it doesn't bust
        '''
        _retVal = 0
        _is_ace = False
        for card in self.hand:
            _retVal += VALUES.get(card.get_rank())
            if card.get_rank() == 'A':
                _is_ace = True
            #endif
        #end_for    
        if _is_ace and _retVal <= 10:
            return _retVal + 10
        else:
            return _retVal
        #endif
    
    def hit(self, deck):
        self.add_card(deck.deal_card())

    def busted(self):
        global busted
        sum = self.get_value()
        if sum > 21:
            return True
        #endif
            
    def draw(self, canvas, _coord_y):
        for card in self.hand:
            card.draw(canvas, 50 + (80*self.hand.index(card)), _coord_y, False)
        #end_for 
        
class Deck:
    '''define deck class'''
    def __init__(self):
        '''add cards back to deck and shuffle'''
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
            #end_for
        #end_for    
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


def deal():
    '''define event handlers for buttons'''
    global outcome, player_points, current, in_play, dealer, player, deck, score
    
    if in_play:
        score -= 1
    #endif

    deck = Deck()
    dealer = Hand()
    player = Hand()
    
    outcome = ""
    player_points = "" 
    current = "Hit or Stand?"
    in_play = True
    
    dealer.hit(deck)
    player.hit(deck)
    
    dealer.hit(deck)
    player.hit(deck)
    
    # outcome = 'You have: ' + str(player.get_value()) + ' points'
    player_points = 'Points: ' + str(player.get_value()) + '.'

def hit():
    global in_play, outcome, score, current, player_points
    
    if in_play == True:
        player.hit(deck)
        # outcome = 'You have: ' + str(player.get_value()) + ' points'
        player_points = 'Points: ' + str(player.get_value()) + '.'
        # if the hand is in play, hit the player
        if player.busted():
            outcome = 'You went bust: ' + str(player.get_value()) + ' points'
            score -= 1
            in_play = False
            current = 'New deal?'
        #endif    
        if player.get_value() == 21:
            player_points = 'Points: ' + str(player.get_value()) + '.'
            outcome = 'You got BLACKJACK!'
            score += 1
            in_play = False
            current = 'New deal?'
        #endif    
    #endif

def stand():
    global outcome, in_play, score, current, player_points
    if in_play == True:
        # outcome = 'You have: ' + str(player.get_value()) + ' points'
        player_points = 'Points: ' + str(player.get_value()) + '.'
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer.get_value() < 17:
            dealer.hit(deck)
            if dealer.busted():
                outcome = "Dealer went bust: " + str(dealer.get_value()) + "."
                score += 1
            #endif 
        #end_while
        
        # assign a message to outcome, update in_play and score        
        if (not dealer.busted()):

            if dealer.get_value() > player.get_value():
                outcome = "Dealer won: "+ str(dealer.get_value()) + ". Your: "+ str(player.get_value())
                score -= 1
            #endif
   
            if dealer.get_value() == player.get_value():
                # outcome = "It's a tie."
                outcome = "It's a tie. You:" + str(player.get_value()) + ". Dealer: "+ str(dealer.get_value())
            #endif

            if dealer.get_value() < player.get_value():
                outcome = "You won: " + str(player.get_value()) + ". Dealer: "+ str(dealer.get_value())
                score += 1
            #endif
        #endif

        print outcome    
        in_play = False
        current = "New deal?"
    #endif
        
# draw handler    
def draw(canvas):
    global in_play
    _text_size = 27
    _text_caption = 40
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Score: " + str(score), (400, 100), _text_size, "Black")
    canvas.draw_text("Blackjack", (50, 100), _text_caption, "Black")
    canvas.draw_text("Dealer", (50, 180), _text_size, "Black")
    canvas.draw_text(outcome, (220, 180), _text_size, "Black")
    canvas.draw_text(player_points, (50, 380), _text_size, "Black")
    canvas.draw_text("Player", (50, 340), _text_size, "Black")
    canvas.draw_text(current, (220, 380), _text_size, "Black")
    dealer.draw(canvas, 200)
    player.draw(canvas, 400)
    card = Card("S", "A")

    if in_play:
        #pass
        card.draw(canvas, 50, 200)
    #endif

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deal()

# get things rolling
frame.start()

# remember to review the gradic rubric


