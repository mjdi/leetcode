# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    @staticmethod
    def increasingTriplet(nums: List[int]) -> bool:
        leng = len(nums)
        if leng < 3:
            return False

        low = nums[0]
        mid = low - 1
        minimum = low

        for i in range(1, leng):
            num = nums[i]
            if num < low and num < minimum:  # update min
                minimum = num
            if num > mid > low:
                # print(f'Found {low=} < {mid=}, {num=}')
                return True
            elif num > minimum:  # new two seq inc
                low = minimum
                mid = num
            # if num equals low or mid, it doesn't matter,
            # since there are already indices to the left
            # in a two seq inc that will contain the same value

            # print(f'{i=}, {nums=}, {minimum=}, {low=}, {mid=}')
        return False

# class Solution:
#     def increasingTriplet(nums: List[int]) -> bool:
#         first_num = float("inf")
#         second_num = float("inf")
#         for n in nums:
#             if n <= first_num:
#                 first_num = n
#             elif n <= second_num:
#                 second_num = n
#             else:
#                 return True
#         return False
