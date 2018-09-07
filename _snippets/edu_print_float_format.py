
I want a to be rounded to 13.95.

>>> a
13.949999999999999
>>> round(a, 2)
13.949999999999999

The round function does not work the way I expected.
python floating-point precision
shareimprove this question

---------
What you can do is modify the output format:

>>> a = 13.95
>>> a
13.949999999999999
>>> print "%.2f" % a
13.95
----------

Hmm... Are you trying to represent currency? If so, you should not be using floats for dollars. You could probably use floats for pennies, or whatever the smallest common unit of currency you are trying to model happens to be, but the best practice is to use a decimal representation, as HUAGHAGUAH suggested in his answer.

It is important not to represent currency in float. Floats are not precise. But penny or cent amounts are integers. Therefore integers are the correct way of representing currency.

I am coming probably too late here, but I wanted to ask, have the developers of Python solved this problem? Because when I do round(13.949999999999999, 2), I simply get 13.95. I have tried it in Python 2.7.6, as well as 3.4. It works. Not sure if 2.7 even was there in 2009. Maybe it is a Python 2.5 thing?

You are running into the old problem with floating point numbers that all numbers cannot be represented. The command line is just showing you the full floating point form from memory. In floating point your rounded version is the same number. Since computers are binary they store floating point numbers as an integer and then divide it by a power of two so 13.95 will be represented in a similar fashion to 125650429603636838/(2**53). Double precision numbers have 53 bits (16 digits) of precision and regular floats have 24 bits (8 digits) of precision. The floating point in python uses double precision to store the values.

for example

  >>> 125650429603636838/(2**53)
  13.949999999999999

  >>> 234042163/(2**24)
  13.949999988079071

  >>> a=13.946
  >>> print(a)
  13.946
  >>> print("%.2f" % a)
  13.95
  >>> round(a,2)
  13.949999999999999
  >>> print("%.2f" % round(a,2))
  13.95
  >>> print("{0:.2f}".format(a))
  13.95
  >>> print("{0:.2f}".format(round(a,2)))
  13.95
  >>> print("{0:.15f}".format(round(a,2)))
  13.949999999999999

If you are after only two decimal places as in currency then you have a couple of better choices use integers and store values in cents not dollars and then divide by 100 to convert to dollars. Or use a fixed point number like decimal

But, what about when the number is going from 13.95 to lets say 13.90.
My output will then be 13.9 I would like it to show the zero

@Christian There is a fundamental difference between the value stored and how you display that value. Formatting the output should allow you to add padding as required, as well as adding comma separators, etc.

worth mention that "%.2f" % round(a,2) you can put in not only in printf, but also in such things like "str()"

why is it that people always assume currency on floating-point rounding? sometimes you just want to work with less precision.

@radtek: You did literally ask for an explanation. The most straightforward solution is indeed to use Decimal, and that was one of the solutions presented in this answer. The other was to convert your quantities to integer and use integer arithmetic. Both of these approaches also appeared in other answers and comments.

There are new format specifications, here:
"http://docs.python.org/library/string.html#format-specification-mini-language"

You can do the same as:

"{0:.2f}".format(13.949999999999999)

Note that the above returns a string. in order to get as float, simply wrap with float(...)

float("{0:.2f}".format(13.949999999999999))

Note that wrapping with float() doesn't change anything:

>>> x = 13.949999999999999999
>>> x
13.95
>>> g = float("{0:.2f}".format(x))
>>> g
13.95
>>> x == g
True
>>> h = round(x, 2)
>>> h
13.95
>>> x == h
True


That will give you a string. Not a number.

to add commas as well you can
    > '{0:,.2f}'.format(1333.949999999)
which prints '1,333.95'.

yes, but you can wrap it with "float()":
    > float("{0:.2f}".format(13.9499999))

@JossefHarush you can wrap it with float(), but you have not gained anything. Now you have a float again, with all the same imprecision. 13.9499999999999 and 13.95 are the same float.

i agree that they are equal, but this limits the float to two decimal points.

Most numbers cannot be exactly represented in floats. If you want to round the number because that is what your mathematical formula or algorithm requires, then you want to use round. If you just want to restrict the display to a certain precision, then do not even use round and just format it as that string. (If you want to display it with some alternate rounding method, and there are tons, then you need to mix the two approaches.)

>>> "%.2f" % 3.14159
'3.14'
>>> "%.2f" % 13.9499999
'13.95'

And lastly, though perhaps most importantly, if you want exact math then you do not want floats at all. The usual example is dealing with money and to store 'cents' as an integer.

exactly what I was looking for. thanks for not assuming that all floating-point rounding questions are about currency.

Try codes below:

>>> a = 0.99334
>>> a = int((a * 100) + 0.5) / 100.0 # Adding 0.5 rounds it up
>>> print a
0.99


If you go with this approach, you should add a 0.5 for a more accurate representation. int(a * 100 + 0.5) / 100.0 ; Using math.ceil is another option. – arhuaco Nov 8 '13 at 0:11

@ShashankSawant: Well, for one thing, the answer as presented does not round, it truncates. The suggestion to add half at the end will round, but then there is no benefit to doing this over just using the round function in the first place. For another thing, because this solution still uses floating point, the OPs original problem remains, even for the "corrected" version of this "solution". 

@interjay which is necessary if the round() does not work as the OP mentioned.

I feel that the simplest approach is to use the format() function.
For example:

a = 13.949999999999999
format(a, '.2f')

13.95

This produces a float number as a string rounded to two decimal points.
shareimprove this answer

note that the return type of this will be a string. this was not what i was looking for.

shareimprove this answer

answered Jan 18 '09 at 18:31
Greg Hewgill
499k1078651037

add a comment
up vote
13
down vote


The python tutorial has an appendix called: Floating Point Arithmetic: Issues and Limitations. Read it. It explains what is happening and why python is doing its best. It has even an example that matches yours. Let me quote a bit:

    >>> 0.1
    0.10000000000000001

    you may be tempted to use the round() function to chop it back to the single digit you expect. But that makes no difference:

    >>> round(0.1, 1)
    0.10000000000000001

    The problem is that the binary floating-point value stored for “0.1” was already the best possible binary approximation to 1/10, so trying to round it again can’t make it better: it was already as good as it gets.

    Another consequence is that since 0.1 is not exactly 1/10, summing ten values of 0.1 may not yield exactly 1.0, either:

    >>> sum = 0.0
    >>> for i in range(10):
    ...     sum += 0.1
    ...
    >>> sum
    0.99999999999999989

One alternative and solution to your problems would be using the decimal module.
shareimprove this answer

answered Jan 19 '09 at 2:05
nosklo
106k31208224

add a comment
up vote
12
down vote


With python < 3 (e.g. 2.6 or 2.7), there are two ways to do so.

# Option one
older_method_string = "%.9f" % numvar

# Option two (note ':' before the '.9f')
newer_method_string = "{:.9f}".format(numvar)

But note that for python versions above 3 (e.g. 3.2 or 3.3), option two is prefered

For more info on option two, I suggest this link on string formatting from the python docs.

And for more info on option one, this link will suffice and has info on the various flags.

Refrence: Convert floating point number to certain precision, then copy to String
shareimprove this answer

edited Jun 29 at 14:18
user465139
1,8091515

answered Dec 11 '13 at 6:37
Clayton
1,9361934



How do you represent an integer? If I use "{i3}".format(numvar) I get an error. – skytux Dec 12 '13 at 15:29


This is what I mean: If numvar=12.456, then "{:.2f}".format(numvar) yields 12.46 but "{:2i}".format(numvar) gives an error and I'm expecting 12. – skytux Dec 12 '13 at 15:47
add a comment
up vote
8
down vote


It's doing exactly what you told it to do, and working correctly. Read more about floating point confusion and maybe try Decimal objects instead.
shareimprove this answer

edited Jan 18 '09 at 18:36
Dana
13.5k124869

answered Jan 18 '09 at 18:33
HUAGHAGUAH
1,49185

add a comment
up vote
6
down vote


The rounding problem has been solved by Python 2.7.0 definitively.

See the Release notes Python 2.7 - Other Language Changes the fourth paragraph:

    Conversions between floating-point numbers and strings are now correctly rounded on most platforms. These conversions occur in many different places: str() on floats and complex numbers; the float and complex constructors; numeric formatting; serializing and de-serializing floats and complex numbers using the marshal, pickle and json modules; parsing of float and imaginary literals in Python code; and Decimal-to-float conversion.

    Related to this, the repr() of a floating-point number x now returns a result based on the shortest decimal string that’s guaranteed to round back to x under correct rounding (with round-half-to-even rounding mode). Previously it gave a string based on rounding x to 17 decimal digits.

The related issue

EDIT - more info:: The formatting of float before Python 2.7 was similar to the current numpy.float64. Both types use the same 64 bit IEEE 754 double precision with 52 bit mantisa. A big difference is that np.float64.__repr__ is formated frequently with an excessive decimal number so that no bit can be lost, but no valid IEEE 754 number exists between 13.949999999999999 and 3.950000000000001, the result is not nice and the conversion repr(float(number_as_string)) is not reversible. On the other side: float.__repr__ is formatted so that every digit is important, the sequence is without gaps and the conversion is reversible. Simply: If you perhaps have a numpy.float64 number, convert it to normal float in order to be formatted for humans not for numeric processors, otherwise nothing more is necessary with Python 2.7+.
shareimprove this answer

edited yesterday
Osmond
92431534

answered Jan 31 at 18:33
hynekcer
4,03712037



Why downvoted? The question was about Python float (double precision) and normal round, not about numpy.double and its conversion to string. Plain Python rounding really can not be done better than in Python 2.7. The most of answers has been written before 2.7, but they are obsoleted, though they were very good originally. This is the reason of my answer. – hynekcer Apr 15 at 11:02
add a comment
up vote
3
down vote


for fix the floating point in type dynamic languages such as Python and Javascript I use this technique

# for example:
a=70000
b=0.14
c=a*b

print c # prints 980.0000000002
#try to fix
c=int(c * 10000)/100000
print c # prints 980

shareimprove this answer

answered Apr 2 '14 at 20:08
Siamand Maroufi
9315

add a comment
up vote
2
down vote


To round a number to a resolution, the best way is the following one, which can work with any resolution (0.01 for 2 decimals or even other steps)

>>> import numpy as np
>>> value = 13.949999999999999
>>> resolution = 0.01
>>> newValue = int(np.round(value/resolution))*resolution
>>> print newValue
13.95

>>> resolution = 0.5
>>> newValue = int(np.round(value/resolution))*resolution
>>> print newValue
14.0

shareimprove this answer

edited Apr 13 at 16:29

answered Aug 26 '15 at 9:17
iblasi
37819



doesn't work for me on python 3.4.3 and numpy 1.9.1 ? >>> import numpy as np >>> res = 0.01 >>> value = 0.184 >>> np.round(value/res) * res 0.17999999999999999 – szeitlin Apr 11 at 16:34
1

Looking for documentation I see the problem comes from numpy.round accuracy/precision. So it requires to define it as int before multiplication with resolution. I updated the code. Thank you for that! – iblasi Apr 13 at 16:28


The only necessary is to convert numpy.float64 result of np.round to float or simply to use round(value, 2). No valid IEEE 754 number exists between 13.949999999999999 (= 1395 / 100.) and 3.950000000000001 (= 1395 * .01). Why do you think that your method is the best? The original value 13.949999999999999289 (= value = round(value, 2)) is even more exact than your 13.95000000000000178 (printed by np.float96). More info also for numpy is now added to my answer that you probably downvoted by mistake. It wasn't about numpy originally. – hynekcer Apr 15 at 13:04


@hynekcer I do not think that my answer is the best. Just wanted to add an example of limit float to n decimals but the nearest of a defined resolution. I checked as you said, that instead of intyou can also use floatfor @szeitlin example. Thank you for your extra comment. (Sorry but I did not downvote you) – iblasi Apr 15 at 20:49
add a comment
up vote
-4
down vote


>>> int(0.999991*100)/100.0
>>> 0.99

shareimprove this answer

edited Jun 1 '15 at 10:57

answered Jun 1 '15 at 10:32
Hassen
3732719



This has already been posted as an answer. This also does not solve the problem effectively. – Jossie Calderon Jul 2 at 2:03
add a comment
up vote
-6
down vote


The method I use is that of string slicing. It's relatively quick and simple.

First, convert the float to a string, the choose the length you would like it to be.

float = str(float)[:5]

In the single line above, we've converted the value to a string, then kept the string only to its first four digits or characters (inclusive).

Hope that helps!
shareimprove this answer

answered Dec 31 '15 at 8:05
tdh
279417

1

Please don't post identical answers to multiple questions. – vaultah Dec 31 '15 at 8:18
7

WOW... tdh... Please never make any accounting software... What happens if the number happen to be 113.94 ?? this would result in 113.9 ... leaving 0.04 missing.... Also this already has answers from over 5 years ago.... – Mayhem Jan 8 at 3:33
add a comment
up vote
-9
down vote


def limit_float(num,len):
    return float(str(num)[:len-1])

shareimprove this answer

edited Apr 19 at 13:37

answered Apr 6 at 15:03
Chris Real
536



This code needs to be edited - it is not valid Python. – gariepy Apr 6 at 20:18
1

Although, it will not work for extremely tiny values (ex: 7.409188262108466e-06) – Antwane Jun 21 at 13:56
add a comment
protected by Community♦ Apr 25 '14 at 5:36

Thank you for your interest in this question. Because it has attracted low-quality or spam answers that had to be removed, posting an answer now requires 10 reputation on this site (the association bonus does not count).

Would you like to answer one of these unanswered questions instead?

asked


7 years ago

viewed


909599 times

active


yesterday

Get the weekly newsletter! In it, you'll get:

    The week's top questions and answers
    Important community announcements
    Questions that need answers

see an example newsletter
Linked
27
python: getting only 1 decimal place
1
how to change 39.54484700000000 to 39.54 and using python
0
Make Python aritmetic operations
1
Floating point addition in Python
0
Too many decimal places when using Java?
-1
How do I limit an output's maximum number of characters?
0
Python float division “rounding error” on division by 100
0
Reducing output file values to 2 decimal places
-1
Floating point decimals in python
1
How to round a float up on 5
see more linked questions…
Related
832
How do I check if a string is a number (float) in Python?
1047
Parse String to Float or Int
1197
Is floating point math broken?
1318
Difference between decimal, float and double in .NET?
91
JavaScript displaying a float to 2 decimal places
6
Floating Point Arithmetic error
3
How to perform unittest for floating point outputs? - python
1
Python+numpy: a lucky floating point case?
0
Work out significant decimal points to format floating point number
3
100 digit floating point python
Hot Network Questions

    Is DRY the enemy of software project management?
    Restrict access to KVM virtual machines to specific users
    Display an overdue task on task list
    Can you take a bath on Mars?
    Is it ok to show up to a conference without registering nor having conference meals?
    Viability of stacking passengers in an airplane cabin
    "President" is to "presidential" as "moderator" is to what?
    Does having a longer Ethernet cable slow your connection?
    Is a acceptable to use the citation references like [1] or [Joh] as nouns in mathematical writing?
    If time travel is possible in the future, no matter how distant, why haven't they come back to tell us?
    Timing Belt need replacing? Unknown mileage
    How often can I do a Minor Action to activate a Goliath's racial power?
    Determine how many times a given number repeats in a list and the positions where this occurs
    The brain-curdling eldritch horrors and the third dimension
    Is the 2-sphere homeomorphic to a topological group?
    Rickrolling in latex (how to hide a message)
    Can you drink a potion one-handed underwater?
    Is there a difference in the meaning of "Kein Zugang" and "Kein Zutritt"?
    What fantasy book series has spells cast by two races using dance-like movements, and many worlds?
    Did any of the Apollo lunar modules land significantly off level?
    Why do many countries in the world still require citizens of states with a high HDI to get visas?
    What kind of attack is prevented by Apache2's error code AH02032 ("Hostname provided via SNI and hostname provided via HTTP are different")?
    Is ～めぇし a possible typo?
    Is it difficult for a GA aircraft to escape a thunderstorm?

question feed
about us tour help blog chat data legal privacy policy work here advertising info mobile contact us feedback
Technology 	Life / Arts 	Culture / Recreation 	Science 	Other

    Stack Overflow
    Server Fault
    Super User
    Web Applications
    Ask Ubuntu
    Webmasters
    Game Development
    TeX - LaTeX



    Programmers
    Unix & Linux
    Ask Different (Apple)
    WordPress Development
    Geographic Information Systems
    Electrical Engineering
    Android Enthusiasts
    Information Security



    Database Administrators
    Drupal Answers
    SharePoint
    User Experience
    Mathematica
    Salesforce
    ExpressionEngine® Answers
    more (13)



    Photography
    Science Fiction & Fantasy
    Graphic Design
    Movies & TV
    Seasoned Advice (cooking)
    Home Improvement
    Personal Finance & Money
    Academia
    more (9)



    English Language & Usage
    Skeptics
    Mi Yodeya (Judaism)
    Travel
    Christianity
    Arqade (gaming)
    Bicycles
    Role-playing Games
    more (21)



    Mathematics
    Cross Validated (stats)
    Theoretical Computer Science
    Physics
    MathOverflow
    Chemistry
    Biology
    more (5)



    Stack Apps
    Meta Stack Exchange
    Area 51
    Stack Overflow Careers

site design / logo © 2016 Stack Exchange Inc; user contributions licensed under cc by-sa 3.0 with attribution required
rev 2016.8.17.3902

