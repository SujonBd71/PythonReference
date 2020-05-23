
# sorted collections in not python core module, its an apache library
# pip install sortedcontainers

import sortedcontainers
from operator import itemgetter, attrgetter

def create_test():
    l = [1,3,2,0,3,-1]
    sl = sortedcontainers.SortedList(l)
    print(sl)

def InSertTest():
    l = [3,2,0,3,-1]
    sl = sortedcontainers.SortedList(l)
    sl.add(1)
    print(sl)

    # to remove
    sl.discard(2)
    #
    
def LowerUpperBound():
    l = [300,200,200,300,-100]
    sl = sortedcontainers.SortedList(l)
    
    print(sl)
    li = sl.bisect_left(200)
    print(sl[li])

    ui = sl.bisect_right(200)
    print(sl[ui])

def SortedListWithComparator():
    l = [[2,'b'], [4, 'c'], [2, 'a'], [1, 'z']]
    sl = sortedcontainers.SortedKeyList(l, key=itemgetter(0,1))
    print(sl)
    
def Tests():
    # create_test()
    # InSertTest()
    # LowerUpperBound()
    SortedListWithComparator()

Tests()

