def test(p):
    l = [1, 2, 3]
    if p == 1:
        return l

    print(l)
    l = [4,5,6]
    return l

l = test(1)
print(l)
l.reverse()


l2 = test(2)
print(l)
print(l2)


c = 1
for i in range(28, 33):
    c = c * i

import math
ncr = math.factorial(36) / math.factorial(36-9)
ncr = ncr / math.factorial(9)

p = c / ncr
print(p)

