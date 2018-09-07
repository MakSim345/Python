#!/usr/bin/env python
# ============================================================
#
#
# ============================================================
#
# ============================================================

# define a decorator function for abstract methods
def abstractmethod(f):
    methodName = f.__name__
    def temp(self, *args, **kwargs):
        raise NotImplementedError( "Attempt to invoke unimplemented abstract method %s" % methodName)
    return temp
