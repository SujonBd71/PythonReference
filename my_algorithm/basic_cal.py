
def calculateqWihoutStack(s):
    t = 0
    import re
    print(s)
    splits = re.split(r'(\(|\)|\+|-|\d+|\s+|\/|\*)', s)
    tokens = []
    for t in splits:
        if len(t.strip()):
            tokens.append(t.strip())
    print(tokens)

    res = 0
    temp = 0
    op = "+"
    for i, t in enumerate(tokens):
        if t[0] in "0123456789":
            if op == "+" or op == "-":
                res = res + temp
                temp = int(t)
                if op == "-":
                    temp = 0 - temp
            else:
                if op == "*":
                    temp*= int(t)
                else:
                    temp//=int(t)
        else:
            op = t
    res = res + temp
    print(res)

def calculate_with_stack(s):
    import re
    splits = re.split(r'(\(|\)|\+|-|\d+|\s+|\/|\*)', s)
    tokens = []
    for t in splits:
        if len(t.strip()):
            tokens.append(t.strip())
    print(tokens)
    l = len(tokens)
    i = 0
    temp = []
    op = "+"
    while i < l:
        t = tokens[i]
        if t not in "+-*/":
            t = int(t)
            if op == "+":
                temp.append(t)
            if op == "-":
                temp.append(0-t)
            if op == "*":
                top = temp.pop()
                temp.append(top * t)
            if op == "/":
                top = temp.pop()
                temp.append(top // t)
        else:
            op = t
        i+=1
    print(sum(temp))
    return sum(temp)

# https://leetcode.com/problems/basic-calculator-iii/discuss/113593/C%2B%2B-Consise-Solution
def calculate_with_bracket(s):
    def cal(tokens, s, e):
        if s > e:
            return 0, e
        temp = []
        i = s
        op = "+"
        print(e)
        while i <= e and tokens[i] != ')':
            print (i)
            t = tokens[i]
            if t == "(":
                n, pos = cal(tokens, i + 1, e)
            else:
                if t in "+-/*":
                    n = 0
                else:
                    n = int(t)
                pos = i + 1
            
            if op == "+":
                temp.append(n)
            if op == "-":
                temp.append(0-n)
            if op == "*":
                top = temp.pop()
                temp.append(top * n)
            if op == "/":
                top = temp.pop()
                temp.append(top // n)
            if pos <= e and tokens[pos] != ')':
                op = tokens[pos]
                i = pos + 1
            else:
                i = pos
            
        res = sum(temp)
        return res, i + 1

    import re
    splits = re.split(r'(\(|\)|\+|-|\d+|\s+|\/|\*)', s)
    tokens = []
    for t in splits:
        if len(t.strip()):
            tokens.append(t.strip())
    print(tokens)
    l = len(tokens)
    res = cal(tokens, 0, l - 1)
    print(res)

s = "10 - 10* 4*2"
calculateqWihoutStack(s)
s = "10 - 10* 4*2"
calculate_with_stack(s)

s = "1 - (-7)"
calculate_with_bracket(s)
