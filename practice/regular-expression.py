import re
import operator

# use \ to split with special characters like + / 

#https://leetcode.com/problems/different-ways-to-add-parentheses/
def nice_arithmatic_exp_parse():
    def diffWaysToCompute(input):
        tokens = re.split('(\D)', input)
        print(tokens)
        nums = map(int, tokens[::2])
        print(nums)
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
       
        print(ops)
    
    s = " 6-4 / 2 "
    diffWaysToCompute(s)





def split_with_delims():
    s =  "10 - (  22 -  3)* 4"
    # s = "110+(205/3)*4-   9"
    import re
   
    # to keep delimeters
    tokens = re.split(r'(\(|\)|\+|-|\d+|\s+|\/|\* )', s)
    print(tokens)

    tokens = re.split(r'\(|\)|\+|-|\d+|\s+|\/|\*', s)
    print(tokens)


    # discarding delimeters
    delims = ["+", "-", "*", "/", "(", ")"]
    pattern = '|'.join(map(re.escape, delims))
    tokens = re.split(pattern,s)
    print(tokens)


def Test():
    str = "$123 rain 345 987 Sp12ain"

    # find single digit match
    x = re.findall("[0-9]", str)
    print(x)

    #find 3 digit numbers
    x = re.findall("[0-9][0-9][0-9]", str)
    print(x)

    str = "The rain in S5pain"
    #Check if the string contains any digits (numbers from 0-9):
    x = re.findall(r"\d", str)
    print(x)

    str = "The rain in Spa+in"
    #Check if the string contains a + :
    x = re.findall("[+]", str)
    print(x)

    str = "The rain in Spain aixfalls mainly in the plain!aixxx"
    #Check if the string contains "ai" followed by 1 or more "x" characters:
    x = re.findall("aix+", str)
    print(x)


    str = "ssds@g.com micheal@mp.com  ssds@g.com  "
    res = re.findall(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)",str)
    print(res)

    # find all email
    str = "12ha-lim@gmail.com  bala  suj.on12@yahoo.com"

    res = re.findall(r'[a-zA-Z]+[\w\.-]*@[\w\.-]+', str)
    print(res)

    # validation
    str = "ha-lim@gmail.com"
    res = re.search(r"^[a-zA-Z]+[\w\.-]*@[\w\.-]+", str)
    print(res)


# Test()

split_with_delims()
#nice_arithmatic_exp_parse()
