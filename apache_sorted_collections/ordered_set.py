import sortedcontainers
from operator import itemgetter, attrgetter

# CRUD
#add, discard, select

def basic_test():
    s = {2, 3, 3, 4, 0, -1}
    st = sortedcontainers.SortedSet(s)

    st.add(1)
    st.add(1)
    li = st.bisect_left(1)
    ui = st.bisect_right(2)
    
    print(st)
    print(li)
    print(ui)
    st.remove(3)
    print(st)

basic_test()
