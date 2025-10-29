# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
from collections import deque
                
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = "+" # mark as visited
        q = deque([(*entrance, 0)])
        while q: # bfs for the shortest path
            x, y, d = q.popleft()
            if (x == 0 or x == m-1 or y == 0 or y == n-1) and [x,y] != entrance:
                return d
            for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx, ny = x + dx, y + dy
                if  0 <= nx < m and 0 <= ny < n and maze[nx][ny] == ".":
                    maze[nx][ny] = "+" # mark as visited
                    q.append((nx, ny, d+1))
        return -1 # ran out of moves and/or found no exits
