# https://leetcode.com/problems/unique-paths/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
                
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def bottom_up_constant_space():
            above_row = [1] * n
            for _ in range(m-1):
                current_row = [1] * n
                for i in range(1,n):
                    current_row[i] = current_row[i-1] + above_row[i] 
                above_row = current_row
            return above_row[-1]
        
        def pascal_inspired_memo():
            if m == 1 and n == 1:
                return 1
            dp = [[0] * n for _ in range(m)]
        
            # view board 45 deg rotated, like a pascal's triangle 
            def gen_45_deg_indices(x): 
                indices = []
                ith,jth = x,0
                for _ in range(1,x+2):
                    if 0 <= ith < m and 0 <= jth < n: # crop bottom corners off  
                        indices.append((ith,jth))
                    ith, jth = ith - 1, jth + 1
                return indices 
            
            dp[0][0] = 1
            dp[m-1][n-1] = -1
            t = 1
            while dp[m-1][n-1] == -1: 
                for i,j in gen_45_deg_indices(t): # sum of left & right diag's paths
                    dp[i][j] = (dp[i-1][j] if 0 <= i-1 < m else 0) + \
                            (dp[i][j-1] if 0 <= j-1 < n else 0) # reccurence eq'n
                t += 1
            
            return dp[m-1][n-1]

        return bottom_up_constant_space()
        return pascal_inspired_memo()