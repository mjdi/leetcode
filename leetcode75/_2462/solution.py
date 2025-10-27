# https://leetcode.com/problems/total-cost-to-hire-k-workers/?envType=study-plan-v2&envId=leetcode-75
from typing import List
from heapq import heapify, heappop, heappush
                
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        lmh = costs[:candidates] # left min heap
        rmh = costs[max(candidates, len(costs)-candidates):]
        heapify(lmh)
        heapify(rmh)
        cost = 0
        l, r = candidates, len(costs) - candidates - 1
        for _ in range(k): 
            if not rmh or lmh and lmh[0] <= rmh[0]:
                cost += heappop(lmh) 
                if l <= r:
                    heappush(lmh, costs[l])
                    l += 1     
            else:
                cost += heappop(rmh)
                if l <= r:
                    heappush(rmh, costs[r])
                    r -= 1     
        return cost

