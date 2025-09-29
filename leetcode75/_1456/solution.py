# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75
                
class Solution:
    @staticmethod
    def maxVowels(s: str, k: int) -> int:
        vowels = 'aeiou'
        if k == 1:  # early return, we just need a single vowel
            return 1 if any([1 if c in vowels else 0 for c in s]) else 0
        maxV = sum([1 if c in vowels else 0 for c in s[0:k]])
        # print(f'i=0, {s[0:k]=}, {maxV=}')
        numV = maxV
        for i in range(1, len(s) - k + 1):
            prevFirst = s[i - 1]
            currLast = s[i + k - 1]
            numV = numV + (1 if currLast in vowels else 0) - (1 if prevFirst in vowels else 0)
            # print(f'{i=}, {s[i:i + k]=}, {prevFirst=}, {currLast=}, {numV=}, Prev{maxV=}')
            maxV = max(maxV, numV)
        # print(f'{maxV=}')
        return maxV
