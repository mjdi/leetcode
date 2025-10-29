# https://leetcode.com/problems/rotting-oranges/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
from collections import deque
                
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count, minutes, m, n, = 0, 0, len(grid), len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    grid[i][j] = 3 # visited and rotten
                    queue.append((i,j,minutes))
                elif grid[i][j] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return minutes
        while queue:
            l = len(queue)
            for _ in range(l):
                x, y, minutes = queue.popleft()
                if grid[x][y] >= 0:
                    grid[x][y] = -grid[x][y] # visited
                    for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                        nx, ny = x+dx, y+dy
                        if (0 <= nx < m and 0 <= ny < n) and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh_count -= 1
                            queue.append((nx, ny, minutes+1)) 
        return minutes if fresh_count == 0 else -1
