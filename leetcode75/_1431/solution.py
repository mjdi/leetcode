# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
                
class Solution:
    @staticmethod
    def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        return [False if i - max(candies) + extraCandies < 0 else True for i in candies]

