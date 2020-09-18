from collections import defaultdict, Counter

def remove_key():
    dic = { 3 :  "three", 4:"four", 5:"five" }
    print(dic)
    dic.pop(4)
    print(dic)

def get_sorted_by_key():
    key_value ={}     
    # Initializing value  
    key_value[2] = 56       
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 

    print(key_value)
    sorted_list = sorted (key_value)
    print(sorted_list)

def inline_initialize():
    dic = { 3 :  "three", 4:"four", 5:"five" }
    print(dic[3])
    print(dic[4])

    dic = {}
    dic[3] = {3:1}
    dic[3][3] +=1
    print(dic[3][3])

def from_list():
    mylist = ["a", "b", "a", "c", "c"]
    dic = dict.fromkeys(mylist, 1)
    print(dic)
    cnt = Counter(mylist)
    print(cnt)

def Test():
    inline_initialize()
    #remove_key()
def test_iteration():
    dic = { 3 :  "three", 4:"four", 5:"five" }
    for i in dic:
        print(i)

def multi_map():
    pass

def CountFreq():
    l = {}
    l["a"] = l.get("a", 0) + 1
    print (l["a"])
    l["a"] = l.get("a", 0) + 1
    print (l["a"])



def test_append():
    dic = defaultdict(list)
    dic["x"].append(1)
    dic["x"].append(2)

    print(dic["x"])




#Test()
#get_sorted_by_key()
#test_iteration()
test_append()


