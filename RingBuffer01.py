#!/usr/bin/env python
# ============================================================
#
#
# ============================================================
# RingBuffer.py
# Implementation of a Cirular Buffer on Python.
# ============================================================

class RingBuffer:
	def __init__(self,size_max):
		self.max = size_max
		self.data = []
	def append(self,x):
		"""append an element at the end of the buffer"""
		self.data.append(x)
		if len(self.data) == self.max:
			self.cur=0
			self.__class__ = RingBufferFull
	def get(self):
  		""" return a list of elements from the oldest to the newest"""
		return self.data

class RingBufferFull:
	def __init__(self,n):
		raise "you should use RingBuffer"
	def append(self,x):		
		self.data[self.cur]=x
		self.cur=(self.cur+1) % self.max
	def get(self):
		return self.data[self.cur:]+self.data[:self.cur]

class RingBuffer2(object):
    """ class that implements a not-yet-full buffer """
    def __init__(self, size_max):
        self.max = size_max
        self.data = [  ]
    class __Full(object):
        """ class that implements a full buffer """
        def append(self, x):
            """ Append an element overwriting the oldest one. """
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def tolist(self):
            """ return list of elements in correct order. """
            return self.data[self.cur:] + self.data[:self.cur]
    def append(self, x):
        """ append an element at the end of the buffer. """
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = __Full
    def tolist(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data

# sample usage
if __name__ == '__main__':
    x = RingBuffer(5)
    x.append(1); x.append(2); x.append(3); x.append(4)
    print x.__class__, x.get( )
    x.append(5)
    print x.__class__, x.get( )
    x.append(6)
    print x.data, x.get( )
    x.append(7); x.append(8); x.append(9); x.append(10)
    print x.data, x.get( )
   
    # sample of use
    #x=RingBuffer(5)
    #x.append(1); x.append(2); x.append(3); x.append(4)
    #print x.__class__,x.get()
    #x.append(5)
    #print x.__class__,x.get()
    #x.append(6)
    #print x.data,x.get()
    #x.append(7); x.append(8); x.append(9); x.append(10)
    #print x.data,x.get()
