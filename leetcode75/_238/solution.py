# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        answer[0] = 1  # nothing left of nums[0]
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]  # prod of nums to the left

        R = 1  # nothing right of nums[-1]
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]  # prod of nums to the right
        return answer

        # def prod(a):
        #     for i in range(1, len(a)):
        #         a[i] = a[i - 1] * a[i]
        #     return a
        # arr = prod(nums[::-1])  # suffix prod
        # arr = arr[::-1]  # reverse
        # nums = prod(nums)  # prefix prod
        # print(f'{arr=}\n{nums=}')
        # nums_i_minus_1 = nums[0]
        # for i in range(0, len(nums)):
        #     if i == 0:
        #         nums[i] = arr[1]  # 2nd largest suffix prod
        #     elif i == len(nums) - 1:
        #         nums[i] = nums_i_minus_1  # 2nd largest prefix prod
        #     else:
        #         arr[i] = nums[i]  # O(1) space use
        #         # prod of adjacent prods (right suffix and left prefix)
        #         nums[i] = nums_i_minus_1 * arr[i + 1]
        #         nums_i_minus_1 = arr[i]

        # return nums  # output array doesn't count as extra space

