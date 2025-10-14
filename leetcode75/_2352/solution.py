# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
from collections import defaultdict
from typing import List
                
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = defaultdict(int)
        for col in list(zip(*grid)):  # turn grid into list of col tuples
            c[col] += 1
        pairs = 0
        for row in grid:
            pairs += c.get(tuple(row), 0)
        return pairs

