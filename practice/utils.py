from operator import itemgetter, attrgetter

def list_conversion():
    A = [1,1,1,0,0,0,1,1,1,1,0]
    s = ''.join([str(elem) for elem in A]) 
    print(s)
    
def enumerate_test():
    import random
    l = [random.randrange(0,100) for i in range(10)]
    
    for counter, value in enumerate(l):
        print(counter, value)
    print()

    for counter, value in enumerate(l, start=2):
        print(counter, value)

    #can be helpful creating tuple
    my_list = ['apple', 'banana', 'grapes', 'pear']
    counter_list = list(enumerate(my_list, 1))
    print(counter_list)

#enumerate_test()



def gen_random():
    import random
    print(random.randrange(1,2,1))

def min_from_list_basic():
    import random
    nums = [random.randrange(0, 1000) for i in range(10)]
    print(nums)
    mn_num = min(nums, key=lambda p: p)
    print(nums.index(mn_num))
    print(mn_num)

def min_from_list_custom():
    # sorting points
    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __str__(self):
            return ("({0},{1})".format(self.x, self.y))

    l = [Point(100, 200), Point(1, 201), Point(10, 20)]
    l.append(Point(11, 25))
    l.append(Point(100, 102))
    
    print(l)
    minx = min(l, key=attrgetter("y", "x"))
    print(minx)

def lamdatest():
    #lamda format
    # lamda x : x + 1
    #here x is input and x + 1 is output


    #since lamda is function it cane be assigned
    lamda_function = lambda x: x + 1
    print( lamda_function(10))

    print((lambda x: x + 1)(20))

def CountInList():
    nums = [1,2,2,3,2,1,1,3]
    print(nums.count(2))
    print(nums.count(3))
    print(nums.count(100))

#lamdatest()
#min_from_list()
#min_from_list_custom()
CountInList()
