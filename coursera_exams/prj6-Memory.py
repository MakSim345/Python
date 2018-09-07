# implementation of card game - Memory

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

class one_card():
    def __init__(self, _number):
        ''' init class'''
        self._str_state = ["closed", "exposed", "open"]        
        self.number = _number # init value
        self.set_closed()
        self.left_bdr = 0
        self.rigth_bdr = 0

    def set_open(self):
        self.state = self._str_state[2]        

    def set_closed(self):
        self.state = self._str_state[0]

    def set_exposed(self):
        self.state = self._str_state[1]            
        
    def get_state(self):
        return self.state   
    
    def get_number(self):
        return self.number

class card_deck():
    def __init__(self):
        ''' init class'''
        self.state = 0 # init value
        self.cards_ctr = 16
        self._max_num = 8
        # self.deck = dict()
        self.label = 0
        self.flip_ctr = 0
    
    def init_deck(self):
        self.cur_exposed_number = -1
        self.flip_ctr = 0
        self._dict = dict()
        self.deck = list()
        
        self.deck_ord = self.gen_deck() + self.gen_deck()        
        self.suffle()

        #convert result dictionary to a list:
        # print self._dict
        for _key in sorted(self._dict): # use SORTED!!!
            print self._dict[_key],
            _tmp = one_card(self._dict[_key])
            self.deck.append(_tmp) 
        #end_for
        
        #init coordinates of each card:
        start = 0
        end = 50
        for card in self.deck:
            card.left_bdr = start
            card.rigth_bdr = end
            end += 50
            start += 50
        #end_for    
        
    def gen_deck(self):
        tmp_deck = list()
        for i in range(self._max_num):
            tmp_deck.append(i)
        return tmp_deck    

    def suffle(self):
        for i in range(self.cards_ctr):
            _origin = True
            while _origin:
                _tmp_number = random.randrange(0, self.cards_ctr)
                if _tmp_number in self._dict:
                    _origin = True
                else:
                    _origin = False
                #endif
            #end_while
            self._dict[_tmp_number] = self.deck_ord[i]
            print self._dict 
        #end_for
        
    def new_game(self):
        self.set_state(0)
        deck.init_deck()
    
    def set_state(self, _new_state):
        self.state = _new_state
        if (_new_state == 2):
            self.flip_ctr += 1
        #endif    
        self.label.set_text("Turns = " + str(self.flip_ctr))    
    
    def exp2open(self):
        for card in self.deck:
            if card.get_state() == "exposed":
                card.set_open()
            #endif    
        #endfor
    
    def exp2close(self):
        for card in self.deck:
            if card.get_state() == "exposed":
                card.set_closed()
            #endif    
        #endfor
    
    # define event handlers
    def mouseclick(self, pos):
        # add game state logic here
        if self.state == 0:
            self.set_state(1)
            for card in self.deck:
                if (card.left_bdr < pos[0]) and  (card.rigth_bdr > pos[0]):
                    card.set_exposed()
                    # print card.number
                    self.cur_exposed_number = card.number
                #endif    
            #endfor
        elif self.state == 1:
            for card in self.deck:
                if (card.left_bdr < pos[0]) and  (card.rigth_bdr > pos[0]):
                    if card.get_state() == "closed":
                        card.set_exposed() # exposed
                        self.set_state(2)
                        if (card.number == self.cur_exposed_number):
                            #well done, now set all exposed cards to open:
                            self.exp2open()
                        #endif        
                    else: #card is open or exposed already, no state change   
                        pass
                    #endif
                #endif        
            #endfor
        else: # state is 2, 
            self.exp2close() # close all exposed cards
            for card in self.deck:
                if (card.left_bdr < pos[0]) and  (card.rigth_bdr > pos[0]):
                    card.set_exposed()
                    self.cur_exposed_number = card.number
                #endif    
            #endfor
            self.set_state(1) 

    # cards are logically 50x100 pixels in size    
    def draw(self, canvas):
        # canvas.draw_text(str(self.state) + " card exposed", [30, 62], 24, "White")
        # draw
        top = 0
        bottom = 99
        start = 0
        n = 5
        end = 50
        line_wdth = 1
        for card in self.deck:
            # print card.get_state() 
            if card.get_state() == "closed":
                canvas.draw_polygon([(start, top), (end, top), (end, bottom), (start, bottom)], line_wdth, 'White', 'Green')    
                # For debug only:
                # canvas.draw_text(str(card.get_number()), (n, 70), 70, 'red')
            else:    
                canvas.draw_text(str(card.get_number()), (n, 70), 70, 'White')
            #endif    
            n +=50
            end += 50
            start += 50
        #end_for

        #canvas.draw_text(str(score2), (460, 50), 30, 'White')
        
# main entrance point:
if __name__ == "__main__":
    print "Main app start"

    deck = card_deck()
    # deck.init_deck()
    # create frame and add a button and labels
    frame = simplegui.create_frame("Memory", 801, 100)
    frame.add_button("Reset", deck.new_game)
    deck.label = frame.add_label("Turns = 0")

    # register event handlers
    frame.set_mouseclick_handler(deck.mouseclick)
    frame.set_draw_handler(deck.draw)

    # get things rolling
    deck.new_game()    
    frame.start()

    print "Main app end."





# Always remember to review the grading rubric