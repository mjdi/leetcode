# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        h = {}
        for n in arr:
            if n not in h:
                h[n] = 1
            else:
                h[n] += 1
        return len(set(h.values())) == len(h.keys())
