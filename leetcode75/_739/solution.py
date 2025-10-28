# https://leetcode.com/problems/daily-temperatures/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotomic stack, greater than variant
        # (not strictly decreasing, duplicates allowed)
        st = []
        days_to_higher_temp = [0] * len(temperatures)
        for curr_day in range(len(temperatures)):
            while len(st) > 0 and temperatures[curr_day] > temperatures[st[-1]]:
                prev_day = st.pop()
                days_to_higher_temp[prev_day] = curr_day - prev_day 
            st.append(curr_day) # add to stack when t[i] <= st[0] 
        return days_to_higher_temp
