# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    @staticmethod
    def largestAltitude(gain: List[int]) -> int:
        prefix = 0
        maxgain = 0
        for i in range(0, len(gain)):
            prefix += gain[i]
            maxgain = max(maxgain, prefix)
        return maxgain