#!/usr/bin/python


import os
import sys
import re

'''
Convert the following English description into code.

    Initialize n to be 1000. Initialize numbers to be a list of numbers from 2 to n, but not including n.
    With results starting as the empty list, repeat the following as long as numbers contains any numbers.
        Add the first number in numbers to the end of results.
        Remove every number in numbers that is evenly divisible by (has no remainder when divided by) the number that you had just added to results.

How long is results?

To test your code, when n is instead 100, the length of results is 25.

'''


class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.penalty = 5
        self.gross_penalty = 0

    def set_penalty(self, _new_penalty_val):
        self.penalty = _new_penalty_val

    def add_gross_penalty(self, _value):
        self.gross_penalty = self.gross_penalty + _value
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance = self.balance + amount

    def withdraw(self, amount):
        '''
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        '''
        self.balance = self.balance - amount        
        if (self.balance < 0):                        
            self.balance = self.balance - self.penalty
            self.add_gross_penalty(self.penalty)
            # print "new balance:", self.balance
        #endif    

    def get_balance(self):
        '''Returns the current balance in the account.'''
        return self.balance

    def get_fees(self):
        '''Returns the total fees ever deducted from the account.'''
        return self.gross_penalty



def unit_test(init_n):
    '''
    - Add the first number in "numbers" to the end of results.
    - Remove every number in numbers that is evenly divisible by (has no remainder when divided by) the number that you had just added to results.
    '''
    n = init_n
    numbers = range(2, n)
    results = range(0)
    
    results.append(numbers[0])


    print numbers
    return results
    
# main entrance point:
if __name__ == "__main__":
    print "Main app start"

    print unit_test(100)

    print "Main app end."


