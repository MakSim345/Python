# Mini-project #6 - Blackjack

import simplegui
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
playerMessage = "Hit or stand?"
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
            print "Invalid card: ", suit, rank

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
        self.cardList = []

    def __str__(self):
        handStr = "Hand contains "
        for eachCard in self.cardList:
            handStr = handStr+eachCard.get_suit()+eachCard.get_rank()+" "
        handStr = handStr.rstrip()        
        return handStr

    def add_card(self, card):
        self.cardList.append(card)

    def get_value(self):
        totalValue = 0
        hasAce = False
        for eachCard in self.cardList:
            currRank = eachCard.get_rank()
            totalValue += VALUES.get(currRank)
            if currRank == 'A':
                hasAce = True
        if hasAce and totalValue<=11:
            totalValue += 10
        return totalValue

    def draw(self, canvas, pos):
        for eachCard in self.cardList:
            eachCard.draw(canvas, pos)
            pos[0] = pos[0]+CARD_SIZE[0]+20

# define deck class 
class Deck:
    def __init__(self):
        self.cardList = []
        for eachSuit in SUITS:
            for eachRank in RANKS:
                self.cardList.append(Card(eachSuit,eachRank));    
    
    def shuffle(self):
        random.shuffle(self.cardList)
        
    def deal_card(self):
        return self.cardList.pop()
        
    def __str__(self):
        deckStr = "Deck contains "
        for eachCard in self.cardList:
            deckStr = deckStr + eachCard.get_suit()+eachCard.get_rank()+" "
        deckStr = deckStr.rstrip()
        return deckStr
deck = Deck()
dealHand = Hand()
playHand = Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealHand, playHand, playerMessage,score
    if in_play:
        outcome = "You lose."
        playerMessage = "New deal?"
        score -= 1
        in_play = False
    else:
        # your code goes here
        currDeck = Deck()
        currDeck.shuffle()
        dealHand = Hand()
        playHand = Hand()
        dealHand.add_card(currDeck.deal_card())
        dealHand.add_card(currDeck.deal_card())
        playHand.add_card(currDeck.deal_card())
        playHand.add_card(currDeck.deal_card())
        print "Play "+str(playHand)
        print "Deal "+str(dealHand)
        playerMessage = "Hit or stand?"
        in_play = True

def hit():
    global playHand,deck,in_play, score,outcome,playerMessage
    if in_play:
        playHand.add_card(deck.deal_card())
        if playHand.get_value() <= 21:
            playMessage = "Hit or stand?"
        else:
            outcome = "You went bust and lose."
            playerMessage = "New deal?"
            score -= 1
            in_play = False
def stand():
    global playHand, dealHand, deck, in_play, score, outcome, playerMessage
    if in_play:
        while dealHand.get_value() <= 17:
            dealHand.add_card(deck.deal_card())
        if dealHand.get_value()>21:
            outcome = "Dealer went bust and you win."
            score += 1
        elif dealHand.get_value() >= playHand.get_value():
            outcome = "You lose."
            score -= 1
        else:
            outcome = "You win."
            score += 1
        playerMessage = "New deal?"
        in_play = False

# draw handler    
def draw(canvas):
    global score,outcome, in_play
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [80,80], 40, "Aqua")
    canvas.draw_text("Score "+str(score), [400,80], 30, "Black")
    canvas.draw_text("Dealer", [60, 150], 30, "Black")
    canvas.draw_text(outcome, [200,150], 30, "Black")
    dealHand.draw(canvas, [55, 180])
    if in_play: 
        tmpCard = Card("C", "2")
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(tmpCard.get_rank()), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(tmpCard.get_suit()))
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [55 + CARD_CENTER[0], 180 + CARD_CENTER[1]], CARD_SIZE)
    canvas.draw_text("Player", [60, 350], 30, "Black")
    canvas.draw_text(playerMessage, [200, 350], 30, "Black")
    playHand.draw(canvas, [55, 380])

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