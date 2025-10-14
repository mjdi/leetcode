# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
                
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
                if i == len(s):
                    return True
        return False
