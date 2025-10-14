# https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            while st and a < 0 and (last := st[-1]) > 0:
                if last <= -a:
                    st.pop()
                if last >= -a:
                    break
            else:
                st.append(a)
        return st
