# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75
from collections import Counter
                
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return ((cnt1 := Counter(word1)).keys() == (cnt2 := Counter(word2)).keys()
                 and sorted(cnt1.values()) == sorted(cnt2.values()))
