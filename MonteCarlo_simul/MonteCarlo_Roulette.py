#!/usr/bin/env python

import random
from datetime import datetime

def test_game(numSpins):
    fr = FairRoulette()
    init_amt = 1000
    
    for i in xrange(numSpins):
        fr.spin()
        init_amt = init_amt + fr.betPocket(1, 10)

    print numSpins, " - (1000). Result:", init_amt


class FairRoulette(object):
    """ FairRoulette implementation """

    def __init__(self):
        self.pockets = []
        
        for i in xrange(1, 37):
            self.pockets.append(i)
        
        self.ball = None
        self.pocketOdds = len(self.pockets) - 1

    def spin(self):
        self.ball = random.choice(self.pockets)
        # print "Got number: ", self.ball
    
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            win_amt = amt*self.pocketOdds
            # print "WINNER! + ", win_amt
            return win_amt
        else:
            # print "LOST! - ", amt
            return -amt 
    
    def __str__(self):
        return "FairRoulette"
     
class EuRoulette(FairRoulette):
    """ EuRoulette implementation """
    def __init__(self):
        FairRoulette.__init__(self)
        # super(FairRoulette, self).__init__()
        self.pockets.append('0')
        
    def __str__(self):
        return " European Roulette"
        
class AmRoulette(EuRoulette):
    """ AmRoulette implementation """
    def __init__(self):
        EuRoulette.__init__(self)
        # super(EuRoulette, self).__init__()
        self.pockets.append('00')
        
    def __str__(self):
        return " American Roulette"

def playRoulette(game, numSpins, pocket, bet):
    totPocket = 0
    for i in xrange(numSpins):
        game.spin()
        totPocket += game.betPocket(pocket, bet)
    res_val = str(100.0*totPocket/numSpins) + ' %\n'
    print (numSpins, 'spins of', game.__str__())
    print 'Expected return betting', pocket, '=', res_val
    return (totPocket/numSpins)

if __name__ == "__main__":    

    print "Roulette start."
    random.seed(datetime.now())
    gameF = FairRoulette()
    gameE = EuRoulette()
    gameA = AmRoulette()

    #for numSpins in (100, 1000000):
    #    for i in xrange(3):
    #        test_game(numSpins)
    
    for numSpins in (100, 1000000):
        for i in xrange(3):
            playRoulette(gameF, numSpins, 7, 1)
            playRoulette(gameE, numSpins, 7, 1)
            playRoulette(gameA, numSpins, 7, 1)

    print "Roulette ends"