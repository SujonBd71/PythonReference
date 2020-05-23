import sortedcontainers
from operator import itemgetter, attrgetter


def create_test():
    d = {10: 1, 20: 2}
    #sd = sortedcontainers.SortedDict(d, key = itemgetter(0))
    sd = sortedcontainers.SortedDict(d)
    sd[4] = 1
    sd[5] = 10
    sd[10] = 10
    sd[20] = 10
    sd[-10] = 10
    
    print(sd)
    lb = sd.bisect_left(10)
    ub = sd.bisect_right(5)
    print(lb)
    print(ub)
    sd.pop(10)
    print(sd)
    
create_test()
