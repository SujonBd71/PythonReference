from collections import namedtuple, Counter, deque, defaultdict
import random
from operator import itemgetter, attrgetter
import re
import copy
import heapq 
import threading

#2D list
ld =  [ [0]*3 for i in range(3)]
ld.sort( key=itemgetter(1,2))
cp = copy.deepcopy(ld)

#collections
c = Counter(['eggs', 'ham', 'ham', 'blue'])
q = deque()
#q operations left means front in C++
q.append(1)
q.appendleft(2)

#heap
li = [23, 32]
def new_cmp_lt(self,a,b):
    return a < b
heapq.cmp_lt=new_cmp_lt
heapq.heapify(li) 
heapq.heappush(li,4) 
heapq.heappop(li)

#named tuple
Fruit = namedtuple("Fruit", ["name", "color", "other"])
f = Fruit(name = "banana", color = "red", other = "notset")

#lamda fuction
lamda_function = lambda x, y: x + y
print( lamda_function(10, 11))

#random
print(random.randrange(1,2,1))

#regular expression
s = " 1 +  1 + 2  / 3 "
t = s.replace(" ", "")
tokens = re.split(r' |\+|\-|\*|\/|\n', s)
res = re.findall(r'[a-zA-Z]+[\w\.-]*@[\w\.-]+', s)
s = "ha-lim@gmail.com"
res = re.search(r"^[a-zA-Z]+[\w\.-]*@[\w\.-]+", s)

#decorator with arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

t1 = threading.Thread(target=print_square, args=(10,)) 
