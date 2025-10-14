# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, maxWindow, lastZero = 0, 0, -1
        for right in range(len(nums)):
            if nums[right] == 0:
                left = lastZero + 1
                lastZero = right
            maxWindow = max(maxWindow, right - left)
        return maxWindow
