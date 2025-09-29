# https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
                
class Solution:
    @staticmethod
    def removeStars(s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] == '*':
                st.pop()
            else:
                st.append(s[i])
        return ''.join(st)
