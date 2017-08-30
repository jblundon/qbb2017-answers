#!/usr/bin/env python

import random

#r = random.randint(1,100)
#print r

#nums = []

#for i in xrange(50):
    #print i
    #r = random.randint(1,100)
    #print "The %dth number is %d" % (i, r)
    #nums.append(r)

#print nums

nums = range(0,100,10)

print nums

key = 20

high = len(nums)
low = 0


while low < high:
    mididx = (low + high) / 2
    mid = nums[mididx]

    print "checking in the range [%d, %d] mididx[%d]=%d" % (low, high, mididx, mid)
    
    if (mid == key):
        print "Hooray! %d==%d at %d" % (key, mid, mididx)
        break
    elif (key > mid):
        low = mididx + 1
    else:
        high = mididx




#for i in xrange(len(nums)):
    #v = nums[i]
    #print "scanning the %dth is %d" % (i,v)
    #if (v == key):
        #print "Found it at position %d" % (i)