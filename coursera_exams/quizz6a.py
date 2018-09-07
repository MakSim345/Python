#!/usr/bin/python


import os
import sys
import re
import os
import sys

'''
 The deposit and withdraw methods each change the account balance. 
 The withdraw method also deducts a fee of 5 dollars from the balance 
 if the withdrawal (before any fees) results in a negative balance. 

 Since we also have the method get_fees, you will need to have a variable to keep track of the fees paid.

Here's one possible test of the class. 
It should print the values 10 and 5, respectively, since the withdrawal incurs a fee of 5 dollars. 
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


def unit_test():
    my_account = BankAccount(10)
    my_account.withdraw(5)
    my_account.deposit(10)
    my_account.withdraw(5)
    my_account.withdraw(15)
    my_account.deposit(20)
    my_account.withdraw(5) 
    my_account.deposit(10)
    my_account.deposit(20)
    my_account.withdraw(15)
    my_account.deposit(30)
    my_account.withdraw(10)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(50) 
    my_account.deposit(30)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.deposit(20)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.deposit(30)
    my_account.withdraw(25) 
    my_account.withdraw(5)
    my_account.deposit(10)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(10) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.deposit(30)
    my_account.withdraw(25) 
    my_account.withdraw(10)
    my_account.deposit(20)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    print my_account.get_balance(), my_account.get_fees()

def unit_test_multi():
    account1 = BankAccount(20)
    account1.deposit(10)
    account2 = BankAccount(10)
    account2.deposit(10)
    account2.withdraw(50)
    account1.withdraw(15)
    account1.withdraw(10)
    account2.deposit(30)
    account2.withdraw(15)
    account1.deposit(5)
    account1.withdraw(10)
    account2.withdraw(10)
    account2.deposit(25)
    account2.withdraw(15)
    account1.deposit(10)
    account1.withdraw(50)
    account2.deposit(25)
    account2.deposit(25)
    account1.deposit(30)
    account2.deposit(10)
    account1.withdraw(15)
    account2.withdraw(10)
    account1.withdraw(10)
    account2.deposit(15)
    account2.deposit(10)
    account2.withdraw(15)
    account1.deposit(15)
    account1.withdraw(20)
    account2.withdraw(10)
    account2.deposit(5)
    account2.withdraw(10)
    account1.deposit(10)
    account1.deposit(20)
    account2.withdraw(10)
    account2.deposit(5)
    account1.withdraw(15)
    account1.withdraw(20)
    account1.deposit(5)
    account2.deposit(10)
    account2.deposit(15)
    account2.deposit(20)
    account1.withdraw(15)
    account2.deposit(10)
    account1.deposit(25)
    account1.deposit(15)
    account1.deposit(10)
    account1.withdraw(10)
    account1.deposit(10)
    account2.deposit(20)
    account2.withdraw(15)
    account1.withdraw(20)
    account1.deposit(5)
    account1.deposit(10)
    account2.withdraw(20)
    print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()

def unit_test_01():
    '''
    Here's one possible test of the class. 
    It should print the values 10 and 5, respectively, since the withdrawal incurs a fee of 5 dollars.
    ''' 
    my_account = BankAccount(10)
    my_account.withdraw(15)
    my_account.deposit(20)
    print my_account.get_balance(), my_account.get_fees()

def unit_test_multi_01():
    '''
    Here's one possible test with multiple accounts. It should print the values 10, 5, 5, and 0
    '''
    account1 = BankAccount(10)
    account1.withdraw(15)
    account2 = BankAccount(15)
    account2.deposit(10)
    account1.deposit(20)
    account2.withdraw(20)
    print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()

# main entrance point:
if __name__ == "__main__":
    print "Main app start"

    unit_test_multi()

    print "Main app end."


