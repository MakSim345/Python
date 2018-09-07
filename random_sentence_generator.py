# goofy sentence generator

import random

def make_sentence(part1, part2, part3, n=1):
    """return n random sentences"""
    # convert to lists
    p1 = part1.split('\n')
    p2 = part2.split('\n')
    p3 = part3.split('\n')
    # shuffle the lists
    random.shuffle(p1)
    random.shuffle(p2)
    random.shuffle(p3)
    # concatinate the sentences
    sentence = []
    for k in range(n):
        try:
            s = p1[k] + ' ' + p2[k] + ' ' + p3[k]
            s = s.capitalize() + '.'
            sentence.append(s)
        except IndexError:
            break
    return sentence

# break a typical sentence into 3 parts
# first part of a sentence (subject)
part1 = """\
a drunken sailor
a giggling goose
the yearning youth
the obese ostrich
this mean mouse
the skinny sister"""

# middle part of a sentence (action)
part2 = """\
jumps over
flies over
runs across
openly ogles
twice tastes
vomits on"""

# ending part of a sentence (object)
part3 = """\
a rusty fence
the laughing cow
the weedcovered backyard
the timid trucker
the rancid old cheese
the jolly jelly"""

print '-'*60

sentence = make_sentence(part1, part2, part3, 3)
for item in sentence:
    print item
print '-'*60

"""
a typical result -->
A drunken sailor flies over the laughing cow.
The obese ostrich runs across the weedcovered backyard.
This mean mouse openly ogles the jolly jelly.
"""