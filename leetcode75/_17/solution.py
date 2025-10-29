# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2a = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
            }
        n = len(digits)
        res = []
        self.sol = ""

        def backtrack(i):
            if i == n:
                res.append(self.sol + "")
                return

            for a in d2a[digits[i]]:
                self.sol = self.sol + a
                backtrack(i+1)
                self.sol = self.sol[:-1] 
            
        backtrack(0) 
        return res

