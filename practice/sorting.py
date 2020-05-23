#  python 2.x has user defined comp options. But it has been removed in python 3.x
# 3.x provides Operator Module. 
# The operator module has itemgetter(), attrgetter(), and a methodcaller() function.


from operator import itemgetter, attrgetter

def BasicSorting():
    l = [[1,2], [1,3], [0,4]]
    l.sort(key=itemgetter(0, 1))
    print(l)

    # reverse ascending on first and decending on second
    l = [[1,2], [1,3], [0,4]]
    l.sort(key=lambda a: (a[0], -a[1]))
    print(l)

    #descending
    l = [[1,2], [1,3], [0,4]]
    l.sort(key=lambda a: (-a[0], -a[1]))
    print(l)


def UserDefined():

    student_tuples = [
    ('john', 'A', 15),
        ('jane', 'D', 12),
        ('dave', 'B', 10),
    ]

    student_tuples.sort( key=itemgetter(0))
    print(student_tuples)

    student_tuples.sort( key=itemgetter(1))
    print(student_tuples)

    student_tuples.sort( key=itemgetter(2))
    print(student_tuples)

    print()
    print("####### sort using multiple ########")
    student_tuples = [
    ('john', 'A', 15),
        ('jane', 'D', 12),
        ('dave', 'D', 10),
    ]


    # multilevel attributes
    student_tuples.sort( key=itemgetter(1,2))
    print(student_tuples)


    # can be sort with name attributes using attrgetter()
    class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age
            
        def __repr__(self):
            return repr((self.name, self.grade, self.age))


    student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]

    print()
    print("#######   sort using name attribute ########")
    student_objects.sort( key=attrgetter("age","grade"))
    print(student_objects)


    print()
    print("#######   sort descending ########")
    student_objects.sort( key=attrgetter("age","grade"), reverse=True)
    print(student_objects)


#python uses only < operation so only that one is enougy

#reference
#https://docs.python.org/3/library/stdtypes.html#list.sort

def  CustomSorting():
    def cmp_to_key(mycmp):
        class K(object):
            def __init__(self, obj, *args):
                self.obj = obj
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
            # def __gt__(self, other):
            #     return mycmp(self.obj, other.obj) > 0
            # def __eq__(self, other):
            #     return mycmp(self.obj, other.obj) == 0
            # def __le__(self, other):
            #     return mycmp(self.obj, other.obj) <= 0  
            # def __ge__(self, other):
            #     return mycmp(self.obj, other.obj) >= 0
            # def __ne__(self, other):
            #     return mycmp(self.obj, other.obj) != 0
        return K
    
    def basic_test():
        def my_cmp(a, b):
            return b - a
        
        l = [1,4,3,2,0,1,5,2,0]
        l.sort(key=cmp_to_key(my_cmp))
        print(l)

    def point_test():
        class Point():
            def __init__(self, x, y):
                self.x = x
                self.y = y
            def __str__(self):
                return ("({0},{1})".format(self.x, self.y))

        l = [Point(100, 200), Point(1, 201), Point(10, 20)]
        l.append(Point(11, 25))
        l.append(Point(100, 102))

        def my_cmp(a, b):
            return a.x - b.x
        l.sort(key=cmp_to_key(my_cmp))

        for p in l:
            print(p)

    #basic_test()
    point_test()


#CustomSorting()
BasicSorting()
#UserObjectWithComparator()

#leetcode 937 ,
#custom sort

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            splits = log.split(" ")
            id_ = splits[0]
            record = splits[1:]
            if record[0].isalpha():
                return (0, record, id_)
            return (1,)
            

        return sorted(logs, key = f)
