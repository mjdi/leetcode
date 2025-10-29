# https://leetcode.com/problems/combination-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, sol, sum):
            if len(sol) == k and sum == n:
                res.append(sol[:])
            elif len(sol) > k or sum > n:
                return

            for next in range(start, 10):
                backtrack(next+1, sol + [next], sum+next) 
            
        backtrack(1, [], 0)
        return res 

