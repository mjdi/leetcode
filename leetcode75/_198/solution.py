# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(0,len(nums)):
            temp = max(nums[i]+rob1, rob2)
            rob1,rob2 = rob2, temp 
        return rob2
