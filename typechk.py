#!/usr/bin/env python

def displayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type: ', type(num).__name__
    else:
        print 'not a numbet at all!!'


displayNumType(-69)
displayNumType(999999999999999999999999)
displayNumType(5+7j)
displayNumType(5.6)
displayNumType('liujiaibn')

