# https://leetcode.com/problems/number-of-provinces/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
                
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            isConnected[city][city] = -1 # has been visited
            for i, c in enumerate(isConnected[city]):
                if isConnected[i][i] != -1 and c == 1: 
                    dfs(i)
                            
        provinces = 0          
        for city in range(len(isConnected)):
            if isConnected[city][city] != -1: # hasn't been visited
                provinces += 1            
                dfs(city)
        
        return provinces

