from collections import deque, Counter, defaultdict
from typing import List
from operator import itemgetter, attrgetter
import copy
import math
import bisect
import heapq

from collections import Counter

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        memo = [[-1] * (n + 10) for i in range(n+1)]
        visit = {}
        smaps = Counter(stones)
 
        def can_Jump(pos, jump):
            
            if jump <=0:
                return False
            if pos not in smaps:
                return False
            
            if pos == n-1:
                return True
            if pos >= n:
                return False
            
            if pos in visit:
                return False
            
            # print(visit)
            visit[pos] = 1

            # if memo[pos][jump] != -1:
            #     return memo[pos][jump]
            
            print(pos)
            print(jump)
            
            res = can_Jump(pos + jump, jump)
            res = res or can_Jump(pos + jump, jump-1)
            res = res or can_Jump(pos + jump, jump+1)
            memo[pos][jump] = res
            return res
     
        res = can_Jump(0, 1)
        print(visit)
        return res
    
            

sol = Solution()
s = "abc"
sf = [0,1,3,5,6,8,12,17]


res = sol.canCross(sf)
print(res)

