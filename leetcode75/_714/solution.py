# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
            T[i][k][0] = max profit on ith day with k transactions with no stock
            T[i][k][1] = ditto but with one stock
            
        """
        Tik0, Tik1 = 0, float("-inf")

        for price in prices:
            # Tik0: not stock or sell stock minus fee; Tik1: rest or buy stock
            Tik0, Tik1 = max(Tik0, Tik1 + price - fee), max(Tik1, Tik0 - price)
        return Tik0

