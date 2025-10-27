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
        g = Binary_Search_Guesser(actual)
        if g.guess(n) == 0:
            return n
        si = [1,n] # search interval
        curr_guess = (si[1] + si[0]) // 2
        while g.guess(curr_guess) != 0:
            if g.guess(curr_guess) == 1: # guess is lower than actual
                si = [curr_guess, si[1]] # search top half
            else: # guess is higher than actual
                si = [si[0], curr_guess] # search bottom half
            curr_guess = (si[1] + si[0]) // 2

        return curr_guess

