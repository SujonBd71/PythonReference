
def split_lines():
    nums= "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    lines = nums.splitlines()
    for l in lines:
        print(l)
    
def stripping():
    nums= "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    lines = nums.splitlines()
    for l in lines:
        name = l.lstrip('\t')
        depth = len(l) - len(name)
        print(name)
        print(len(l))
        print(len(name))

def replace():
    string = "geeks for geeks geeks geeks geeks" 
    # Prints the string by replacing geeks by Geeks  
    print(string.replace(" ", ""))  
    # Prints the string by replacing only 3 occurrence of Geeks   
    print(string.replace("geeks", "GeeksforGeeks", 3)) 


def ASCI_Value():
    a = 'a'
    print(a)
    int_a = ord(a)
    print(int_a)
    b_char = chr(int_a)
    print(b_char)

def mathmatics():
    string = '123456'
    print( string.isnumeric()) 

def IntListToString():
    l = [1, 23, 0, -1]
    s = [str(n) for n in l]
    print(s)
    ss = ";".join(s)

    print(ss)


# split_lines()
# stripping()

# replace()
#ASCI_Value()
IntListToString()

