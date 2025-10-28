# https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
                
class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0,1,1]
        if n < len(t):
            return t[n]
        for i in range(3,n+1):
            t.append(t[i-1] + t[i-2] + t[i-3])
        return t[n]
