# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
                
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)
        while l<=r:
            m = l + ((r-l) // 2)
            if m > 0 and nums[m] < nums[m-1]:
                r = m - 1 # there is a peak in the left section
            elif m < len(nums) - 1 and nums[m] < nums[m+1]:
                l = m + 1 # there is a peak in the right section
            else: # thus nums[m] is greater than its neighbors
                return m # always guarenteed to have a peak