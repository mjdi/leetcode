# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
                
class Solution:
    def reverseVowels(self, s: str) -> str:
        # two pointers
        ss = list(s)
        vowels = list('aeiouAEIOU')
        l, r = 0, len(s) - 1
        while l <= r:
            if l == r:
                break
            if ss[l] in vowels and ss[r] in vowels:
                temp = ss[l]
                ss[l] = ss[r]
                ss[r] = temp
            elif ss[r] in vowels:
                r += 1
            elif ss[l] in vowels:
                l -= 1
            l += 1
            r -= 1
        return "".join(ss)
