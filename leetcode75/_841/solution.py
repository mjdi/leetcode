# https://leetcode.com/problems/keys-and-rooms/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
        
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = {i:False for i in range(len(rooms))}
        
        def dfs(room_num):
            self.visited[room_num] = True
            for key in rooms[room_num]:
                if not self.visited[key]:
                    dfs(key)

        dfs(0) # we can enter room 0 without a key
        
        return all(self.visited.values()) 

