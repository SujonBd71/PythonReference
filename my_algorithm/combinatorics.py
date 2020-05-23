
def nCr(n, r):
    import math
    d = max(r, n - r)
    res = math.factorial(n) / math.factorial(d)
    return res / math.factorial(n-d)

for i in range(5):
    print(nCr(5,i))


print(nCr(32, 5) / nCr(36, 9))
