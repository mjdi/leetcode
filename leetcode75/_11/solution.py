# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        height
        l, r = 0, len(height) - 1
        maxl, maxr, maxv = height[l], height[r], min(height[l], height[r]) * (r - l)

        if maxr >= maxl:
            l += 1
        else:
            r -= 1

        while r > l:
            h = min(height[l], height[r])
            w = r - l
            v = h * w
            maxv = max(maxv, v)
            maxl = max(maxl, height[l])
            maxr = max(maxr, height[r])

            if maxr >= maxl:
                l += 1
            else:
                r -= 1

        return maxv
