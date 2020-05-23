
def CreateFromDic():
    dic = { 3 :  "three", 4:"four", 5:"five" }
    print(dic)
    l = list(dic.keys())
    print(l)

CreateFromDic()


def Create2DList():   
    # this is proper way to create with initial values
    ld =  [ [0]*3 for i in range(3)]
    for i in range(0,3):
        print(ld[i])
    
    ld[1][2] = -100
    for i in range(0,3):
        print(ld[i])

    # double list
    # doing this is a hell , you will be in trap,
    la = [-1] * 5
    ld = [la] * 3
    print("### 2D list")
    for i in range(0,3):
        print(ld[i])

    # see the hell hear, if you change one cell it will change al
    ld[1][2] = -100
    print("### 2D list after chaning 1 cell, surprised??")
    for i in range(0,3):
        print(ld[i])

    # this is the also bad
    print("### 2D list bad again")
    la = [-1] * 10
    ld = [la for i in range(0,3)]
    for i in range(0,3):
        print(ld[i])
    ld[1][2] = -100
    for i in range(0,3):
        print(ld[i])

def ListOperations():
    #this one line code remove duplicaes creating dic
    mylist = ["a", "b", "a", "c", "c"]
    mylist = list(dict.fromkeys(mylist))
    print(mylist)

     #revese
    l = [1,2,3,4,5]
    lr = l.reverse()
    print(l)
    print(lr)

    #search
    vowels = ['a', 'e', 'i', 'o', 'i', 'u']
    index = vowels.index('e')
    print('The index of e:', index)

    
def ListSlice():
    # items start through the end using step (but the end is not included!)
    # a[start:end:step] , step is optional , default is 1
    l = [1,2,3,4,5,6]
    full_copy = l[:] 
    print(full_copy)
    # first index inclusize but last index not included
    sub = l[2:5] 
    print(sub)
    # copy everything using given step i.e 2 
    sub = l[::2]
    print(sub)


def ListDeepCopy():
    a = [[1, 2, 3], [4, 5, 6]]
    # this is shallo copy and bad
    b = list(a)
    print("List a")
    print(a)
    a[0][1] = -999

    print("list b")
    print(b)
    print("lis b is changed, but we changed list a")

    import copy
    a = [[1, 2, 3], [4, 5, 6]]
    print("List a")
    print(a)
    b = copy.deepcopy(a)
    a[0][1] = -999
    print("List b after channg a")
    print(b)

def Tests():
    #ListDeepCopy()
    ListOperations()

Tests()
