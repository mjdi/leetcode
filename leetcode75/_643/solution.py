# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # as the window slides, we subtract the previous first num in sliding window
        # and add the newest last num in the window, comparing new average to maxAvg
        currSum = sum(nums[0:k])  # i = 0
        maxAvg = currSum / k
        for i in range(1, len(nums) - k + 1):
            currSum = currSum + nums[i + k - 1] - nums[i - 1]
            maxAvg = max(maxAvg, currSum / k)
        return maxAvg
