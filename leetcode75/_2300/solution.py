# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions = sorted(potions)

        def binary_search(spell, potions, success):
            l,r = 0, len(potions)
            # we want to find the threshold index where potency >= success
            # potency[x] = spell * potions[x]
            while l<r:
                m = (l+r)//2
                potency = spell * potions[m]
                if potency < success:
                    l = m + 1 
                else:
                    r = m - 1
            if spell * potions[r] < success:
                return len(potions) - 1 - r 
            return len(potions) - max(r,0) # r can be -1 if len(potions) is 1
 

        for s in spells:
            if s * potions[-1] < success:
                pairs.append(0)
                continue
            pairs.append(binary_search(s, potions, success))
        return pairs

