# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    @staticmethod
    def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = {n: n for n in nums1}
        list2 = {n: n for n in nums2}
        for n in nums2:
            if n in list1:
                del list1[n]
        for n in nums1:
            if n in list2:
                del list2[n]
        return [list(list1), list(list2)]
