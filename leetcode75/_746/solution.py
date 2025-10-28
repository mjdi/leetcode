# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def recursive(): # top down, time: O(2^n), space: O(1) 
            def dp(n):
                if n < 2:
                    return cost[n] 
                return cost[n] + min(dp(n-1), dp(n-2))
            length = len(cost) 
            return min(dp(length-1), dp(length-2))


        def bottom_up_tabulation(): # time: O(n), space: O(n)
            n = len(cost) 
            dp = [0] * (n+1)
            dp[0], dp[1] = cost[0], cost[1]
            
            for i in range(2,n):
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            return min(dp[n-1], dp[n-2])


        def bottom_up_tabulation_constant_space(): # time: O(n), space: O(1)
            n = len(cost) 
            dp_1, dp_2 = cost[0], cost[1]
            for i in range(2,n):
                temp = dp_2
                dp_2 = cost[i] + min(dp_1, dp_2)
                dp_1 = temp
            return min(dp_1,dp_2)


        def top_down_memoization(): # time: O(n), space: O(n)
            n = len(cost)
            dp = [0] * (n+1)
            dp[n-1], dp[n-2] = cost[n-1], cost[n-2]
            for i in range(n-3,-1,-1): # reverse order
                dp[i] = cost[i] + min(dp[i+1], dp[i+2]) 
            return min(dp[0], dp[1])

        # return recursive()
        # return bottom_up_tabulation()
        # return bottom_up_tabulation_constant_space() # most efficient
        return top_down_memoization()
