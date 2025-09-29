# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75p
from typing import List
                
class Solution:
    @staticmethod
    def pivotIndex(nums: List[int]) -> int:
        leftsum, S = 0, sum(nums)
        for i in range(len(nums)):
            if S - leftsum - nums[i] == leftsum:
                return i
            leftsum += nums[i]
        return -1
