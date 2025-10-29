# https://leetcode.com/problems/online-stock-span/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional

class StockSpanner:
    def __init__(self):
        # Stack stores pairs (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        # merge spans as we pop from the monotomically decreasing stack
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price, span)) # always new smallest price on stack
        return span
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
  