# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    @staticmethod
    def mergeAlternately(word1: str, word2: str) -> str:
        i, j = 0, 0
        merged = ""
        while i < len(word1) or j < len(word2):
            if i == len(word1):
                merged += word2[j:]
                break
            elif i < len(word1):
                merged += word1[i]
                i += 1

            if j == len(word2):
                merged += word1[i:]
                break
            elif j < len(word2):
                merged += word2[j]
                j += 1

        return merged
