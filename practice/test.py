from collections import deque, Counter, defaultdict
from typing import List
from operator import itemgetter, attrgetter
import copy
import math
import bisect
import heapq

from collections import Counter

from operator import itemgetter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        freq =  Counter(s)
        wfreq = {}
        print(freq)   
        n = len(s)
        l = 0
        r = 0
        i = 0
        while i < n:
            r = i
            wfreq[s[r]] 




sol = Solution()
s = "aaabb"
k = 3

res = sol.longestSubstring(s, k)
print(res)

