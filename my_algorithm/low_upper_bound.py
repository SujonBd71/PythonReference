def lower_bound(a, x, l=0, h=None):
    if h == None:
        h = len(a)

    while l < h:
        m = (l + h) >> 1
        if a[m] < x:
            l = m + 1
        else:
            h = m
        
    return l

print(lower_bound([0], 0))


def upper_bound(a, x, l=0, h=None):
    if h == None:
        h = len(a)

    while l < h:
        m = (l + h) >> 1
        if a[m] > x:
            h = m
        else:
            l = m + 1
        
    return l


def Tests():
    a = []
    for i in range(100):
        a.append(i)
    
    for i in range(10):
        import random
        ind = random.randrange(0, 100)
        print(ind)
        print("low: " + str(lower_bound(a,ind)))
        print("up: " + str(upper_bound(a,ind)))
    
    print("up: " + str(upper_bound(a,8)))
    print("up: " + str(upper_bound(a,9)))
    print("up: " + str(lower_bound(a,0)))
    print("up: " + str(lower_bound(a,-1)))
    
Tests()
