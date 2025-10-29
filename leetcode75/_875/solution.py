# https://leetcode.com/problems/koko-eating-bananas/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
import math
                
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        
        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)            
            return hours <= h 
        
        while l < r:
            k = l + (r-l) //2
            if k_works(k):
                r = k # want to include working value of k
            else:
                l = k + 1
        return r 
