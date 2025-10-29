# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
                
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # build adj lists
        self.visited = {}
        self.num_reorders = 0 
        self.adj = []
        
        for _ in range(n):
            self.adj.append([])
        
        for c in connections:
            c1, c2 = c[0], c[1]
            # since dfs from city zero, need all outward connections to flip inwards
            self.adj[c1].append(-c2) 
            self.adj[c2].append(c1)

        def dfs(city):
            if city not in self.visited:
                self.visited[city] = True
            for a in self.adj[city]:
                if abs(a) not in self.visited:
                    if a < 0:
                        self.num_reorders += 1
                    dfs(abs(a))
        dfs(0)    
        
        return self.num_reorders

