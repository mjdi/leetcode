# https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75
from collections import deque 
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rcount = senate.count("R")
        dcount = len(senate) - rcount
        r_floating_bans, d_floating_bans = 0, 0
        q = deque(senate)

        while rcount and dcount:
            s = q.popleft()

            if s == "R":
                if r_floating_bans:
                    r_floating_bans -= 1
                    rcount -= 1
                else:
                    d_floating_bans += 1
                    q.append("R")
            else:
                if d_floating_bans:
                    d_floating_bans -= 1
                    dcount -= 1
                else:
                    r_floating_bans += 1
                    q.append("D")

        return "Radiant" if rcount else "Dire"
