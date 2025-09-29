# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    @staticmethod
    def maxOperations(nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums = sorted(nums)
        l, r = 0, len(nums) - 1
        while nums[r] >= k:
            r -= 1
            if r == 0:
                return 0
        numops = 0
        while r > l:
            if nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:  # sum equals k
                numops += 1
                l += 1
                r -= 1
        return numops
