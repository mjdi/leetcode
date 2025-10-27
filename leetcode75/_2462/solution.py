# https://leetcode.com/problems/total-cost-to-hire-k-workers/?envType=study-plan-v2&envId=leetcode-75
from typing import List
import heapq
                
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l,r = 0, len(costs) - 1
        cost = 0
        lminheap, rminheap = [], []
        while k > 0 :
            while r >= l and (len(lminheap) < candidates or len(rminheap) < candidates):
                if len(lminheap) < candidates and l <= r:
                    heapq.heappush(lminheap, costs[l])
                    l += 1
                if len(rminheap) < candidates and r >= l:
                    heapq.heappush(rminheap, costs[r])
                    r -= 1
                if l == r-1:
                    print("debug")
                    
              
            lmincost = heapq.heappop(lminheap) if len(lminheap) > 0 else float("inf")
            rmincost = heapq.heappop(rminheap) if len(rminheap) > 0 else float("inf")

            if lmincost <= rmincost and lmincost != float:
                cost += lmincost 
                if rmincost != float("inf"):
                    heapq.heappush(rminheap, rmincost)
            else:
                cost += rmincost
                if lmincost != float("inf"):
                    heapq.heappush(lminheap, lmincost)
                
            k -= 1
            
        return cost

