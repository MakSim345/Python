import os
import sys
import re
import os
import sys

"""
The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite length of time will almost surely type out a given text, such as the complete works of John Wallis, or more likely, a Dan Brown novel.

Let's suppose our monkeys are typing, typing and typing, and have produced a wide variety of short text segments. Let's try to check them for sensible word inclusions.

You are given some text potentially including sensible words. You should count how many words are included in the given text. A word should be whole and may be a part of other word. Text letter case does not matter. Words are given in lowercase and don't repeat. If a word appears several times in the text, it should be counted only once.

For example, text - "How aresjfhdskfhskd you?", words - ("how", "are", "you", "hello"). The result will be 3.

Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).

Output: The number of words in the text as an integer.

count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}) == 1

Precondition:
0 < len(text) =< 256
all(3 =< len(w) and w.islower() and w.isalpha for w in words) 

"""

def checkio_2(els):
    a = 0
    for i in range(3):
        a = a + els[i]
    return a

def checkio(_string_to_check):
    print ("string to check:", _string_to_check)
    a = 0
    _dict = {}
    _max_n = 0
    _ret_letter = ''

    #ignore case:
    _string_to_check = _string_to_check.lower()

    # fill dictionary with letters and freq:
    for i in range(len(_string_to_check)):
        a = _string_to_check[i]
        if str.isalpha(a): # letters only!
            if (a in _dict):
                _dict[a] = _dict[a] + 1
            else:
                _dict[a] = 1
            #endif
        #endif
    #endfor

    for key in sorted(_dict):
        print ("%s: %s" % (key, _dict[key]))
        if _max_n < _dict[key]:
            _max_n = _dict[key]
            _ret_letter = key
            print ("New favourite: %s: %s" % (_max_n, _ret_letter))
        #endif
    #endfor

    return _ret_letter


def checkio_2(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

def checkio_3(text):
    text = ''.join(i for i in text.lower() if i.isalpha())
    return max(set(text), key=text.count)

#============================================
def count_words(text, words):
    """ text: str, words: set
        output: int """    
    ret_value = 0
    print "Input text:", text
    text_to_handle = text.lower()
    for i in words:
        print i
        if i in text_to_handle:
            print i ," is in text!"
            ret_value = ret_value + 1
    return ret_value

# main entrance point:
if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                      {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    print ""
    print "Main program end."
