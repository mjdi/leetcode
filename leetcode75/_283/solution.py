# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    @staticmethod
    # def moveZeroes(nums: List[int]) -> None:
    def moveZeroes(nums: List[int]) -> List:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            if nums[i] != 0:
                i += 1

        return nums
