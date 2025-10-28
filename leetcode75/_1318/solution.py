# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
import math
                
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for _ in range(math.ceil(math.log(max(a,b,c),2))+1): 
            alsb = a & 1
            blsb = b & 1
            clsb = c & 1
            
            if clsb == 1:
                if alsb == 0 and blsb == 0:
                    flips += 1
            else: # clsb == 0
                if alsb == 1 and blsb == 1:
                    flips += 2
                elif alsb == 1 or blsb == 1:
                    flips += 1
            a >>= 1 
            b >>= 1 
            c >>= 1 
        return flips


