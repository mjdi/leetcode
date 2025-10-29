# https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
                
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # https://www.youtube.com/watch?v=NnD96abizww
        # create matrix with text1 and text2 on each axis, and compare letter by letter
        # padded by an extra row and column of zeros at the top left
        n1, n2 = len(text1), len(text2)
        u,v = [0] * (n2+1), [0] * (n2+1)
        for i in range (1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1] == text2[j-1]: # case 1
                    v[j] = u[j-1] + 1 
                else:
                    v[j] = max(v[j-1], u[j])
            current = v
            v,u = u,current 
        return u[-1]
