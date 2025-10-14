# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while True:
            i = 0
            while i < len(str1) and i < len(str2):
                if str1[i] == str2[i]:
                    i += 1
                else:
                    return ""
            if len(str1) == len(str2):
                return str1
            # replace the longer string with its excess
            elif len(str1) > len(str2):
                str1 = str1[i:]
            else:
                str2 = str2[i:]

