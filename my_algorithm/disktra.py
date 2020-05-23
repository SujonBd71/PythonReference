
#leetcode 743. Network Delay Time

#this algorithm doesn't stop once it finds the target, it calculates all distance

from collections import deque, Counter, defaultdict
from typing import List
from operator import itemgetter, attrgetter
import copy
import math
import bisect
import heapq

class Solution:
    def networkDelayTime(self, times, N, s):
        edges = defaultdict(list)
        for u,v,w in times:
            edges[u].append([v,w])
        
        dist = {}
        pq = [[0, s]]
        while len(pq):
            d, u = heapq.heappop(pq)
            if u in dist:continue

            dist[u] = d
            for v,w in edges[u]:
                if v not in dist:
                    heapq.heappush(pq, [d + w, v])

        if len(dist) != N:
            return -1
        return max(dist.values())