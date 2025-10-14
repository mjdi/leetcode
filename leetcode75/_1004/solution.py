# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # class Solution:
        #     def longestOnes(self, nums: List[int], k: int) -> int:
        #         left = 0
        #         for right in range(len(nums)):
        #             # If we included a zero in the window we reduce the value of k.
        #             # Since k is the maximum zeros allowed in a window.
        #             k -= 1 - nums[right]
        #             # A negative k denotes we have consumed all allowed flips and window has
        #             # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
        #             if k < 0:
        #                 # If the left element to be thrown out is zero we increase k.
        #                 k += 1 - nums[left]
        #                 left += 1
        #         return right - left + 1

        leftZptr = 0
        i = 0
        numZerosSeen = 0
        numOnesSeen = 0
        maxConsecOnes = 0
        while i < len(nums):
            if nums[i] == 0:
                numZerosSeen += 1
                # move leftZptr until numOnesSeen == k
                # subtracting from numOnesSeen as appropriate
                if numZerosSeen > k:
                    if nums[leftZptr] == 0:
                        leftZptr += 1
                    else:  # find next zero after current group of ones, and pass it
                        while nums[leftZptr] != 0:
                            numOnesSeen -= 1
                            leftZptr += 1
                        # have now hit the first zero past the 1's group
                        leftZptr += 1
                    numZerosSeen -= 1
            else:
                numOnesSeen += 1
            maxConsecOnes = max(maxConsecOnes, (i + 1) - leftZptr)
            i += 1
            # print(f'{leftZptr=}, {i=}, {numOnesSeen=}, {numZerosSeen=}, {maxConsecOnes=}, {nums[leftZptr:i]=}')
        return maxConsecOnes
