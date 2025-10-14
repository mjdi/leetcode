# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if i == 0 and flowerbed[0] == 0:
                if len(flowerbed) == 1:
                    flowerbed[0] = 1  # plant flower at first plot
                    n -= 1
                if len(flowerbed) > 1 and flowerbed[1] == 0:
                    flowerbed[0] = 1  # plant flower at first plot
                    n -= 1
            elif flowerbed[i - 1] == 0 and flowerbed[i] == 0:  # i > 0
                if i == len(flowerbed) - 1:
                    flowerbed[i] = 1  # plant flower at last plot
                    n -= 1
                elif flowerbed[i + 1] == 0:
                    flowerbed[i] = 1  # plant flower at current plot
                    n -= 1
            i += 1
        return n <= 0
