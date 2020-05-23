import bisect

def basic():
    nums = [10,20,30,30,40,40,50]
    l = bisect.bisect_left(nums, 35)
    r = bisect.bisect_right(nums, 30)
    print(l)
    print(r)

def on_list():
    nums = [('a', 5), ('b', 1), ('c', 8), ('c', 20), ('d', 0)]

    l = bisect.bisect_left(nums, 35)
    r = bisect.bisect_right(nums, 35)
    print(l)
    print(r)


def Test():
    basic()

Test()

