# https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = (n+1) * [0]
        
        for i in range(1, n+1):
             term1 = res[i >> 1] # term1 = res[i // 2]
             term2 = (i & 1) # term 2 = 1 if i % 2 == 1 else 0 
             res[i] = term1 + term2

        # x=1
        # power=1
        # for i in range(1,n+1):
        #     if power == i:
        #         power *=2
        #         x = i
        #     #numBits = k + 2^power given that k < 2^power 
        #     res[i] = res[i-x] + 1 # res[i-x]: k; 1: 2^power           
        return res
