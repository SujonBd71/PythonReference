
import collections

def simpletest():
    q = collections.deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    q.pop()
    print(q)

    # print lefmost, i.e fist in the que
    print(q[0])
    # print rightmost, i.e last inserted
    print(q[-1])

    # process first in the que
    q.popleft()
    print(q)

    q = collections.deque([10, 20, 30])
    print(q[0])

def post_order(): 
    q = collections.deque()
    root = []
    q.append(root)
    cur = root
    while (len(q) > 0 or cur != None):
        if (cur is not None):
            q.append(cur.left)
        else:
            top = q.p


simpletest()
