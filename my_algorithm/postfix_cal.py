from collections import deque, Counter
from typing import List
from operator import itemgetter, attrgetter
import copy
import math
import bisect
import heapq

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        import re
        tokens = re.split(r'(\+|-|\*|\/|\(|\)|\s)', s)
        print(tokens)
        
        def evaluate(tokens):
            stk = []
            operators = ["+", "-", "*", "/"]
            for t in tokens:
                if t not in operators:
                    stk.append(t)
                    continue
                b = int(stk[-1])
                stk.pop()
                a = int(stk[-1])
                stk.pop()

                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a*b
                else:
                    res = a / b
                print(str(a) + " " + str(b))
                stk.append(str(res))
                print(res)

            return stk[-1]
                
        def convert_postfix(tokens):
            tokens.insert(0, "(")
            tokens.append(")")

            output = []
            stk = []
            prec = { "+":1, "-":1, "*":2, "/":2  }
            operators = ["+", "-", "*", "/"]
            for t in tokens:
                if t in operators:
                    while len(stk) > 0:
                        top = stk[-1]
                        if top == "(" or prec[top] < prec[t]:
                            break
                       
                        output.append(top)
                        stk.pop()
                    stk.append(t)

                elif t == "(":
                    stk.append(t)
                
                elif t == ")":
                    while len(stk) > 0 and stk[-1] != '(':
                        output.append(stk[-1])
                        stk.pop()
                    stk.pop()
                elif len(t)>0:
                    output.append(t)
            while len(stk):
                output.append(stk[-1])
                stk.pop()
            
            return output
      
        postfix = convert_postfix(tokens)
        print(postfix)
        res = evaluate(postfix)
        return res

                 
sol = Solution()
nums = " 2-1 +         (2 -3) * 4 "
res = sol.calculate(nums)
print(res)
