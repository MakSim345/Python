#### Making a dictionary ####
data = {}
# OR #
data = dict()

#### Initially adding values ####
data = {'a':1,'b':2,'c':3}
# OR #
data = dict(a=1, b=2, c=3)

#### Inserting/Updating value ####
data['a']=1  # updates if 'a' exists, else adds 'a'
# OR #
data.update({'a':1})
# OR #
data.update(dict(a=1))
# OR #
data.update(a=1)
# OR #
data.update([(a,1)])

#### Merging 2 dictionaries ####
data.update(data2)  # Where data2 is also a dict.

# check if value is on dict:
d = {'1': 'one', '3': 'three', '2': 'two', '5': 'five', '4': 'four'}
print 'one' in d.values()

# check if key is on dict:
d = {'1': 'one', '3': 'three', '2': 'two', '5': 'five', '4': 'four'}
print '1' in d