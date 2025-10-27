# https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Binary_Search_Guesser:
    def __init__(self, actual:int ):
        self.actual = actual
        
    def guess(self, gguess):
        if gguess == self.actual:
            return 0
        elif gguess > self.actual:
            return -1
        else: 
            return 1
  
class Solution:
    def guessNumber(self, n: int, actual:int) -> int:
        bsg = Binary_Search_Guesser(actual)
        l,r = 1,n 
        while l <= r:
            m = (l+r) //2 #
            g = bsg.guess(m)
            if g == 0: 
                return m
            elif g == -1: # guess is too high
                r = m - 1
            else: # guess is too low, g == 1
                l = m + 1
        return l
