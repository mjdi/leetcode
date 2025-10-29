# https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        return xor
# It is hard to grasp the intuition behind solution #4, bear in mind that
# XOR operation is commutative and associative, meaning that when we xor 
# all element in the nums list, we can rearrange them so that two identical 
# element sitting next to each other and xor ing them result in 0.
# Example:
# 1 xor 2 xor 3 xor 1 xor 2 xor 3 xor 4 = (1 xor 1) xor (2 xor 2) xor (3 xor 3) xor 4 (commutative & associative)
# = 0 xor 0 xor 0 xor 4
# = 4