# https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
import heapq 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
# Quick Select algo: Neetcode: https://www.youtube.com/watch?v=XEmy13g1Qxc
# https://en.wikipedia.org/wiki/Quickselect
# O(N), worst case O(N^2)

# Max/Min heap solutions: https://www.youtube.com/watch?v=ZmGk7h8KZLs
        # Max heap of size N
        # Time: O(N + k log N)
        # Space O(1)

        # for i in range(len(nums)):
        #     nums[i] = -nums[i]
            
        # heapq.heapify(nums)
        
        # for _ in range(k-1):
        #     heapq.heappop(nums)

        # return - heapq.heappop(nums)  

        # Min heap of size k
        # Time: O(n log k)
        # Space: O(k)
        
        min_heap = []
        
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
            
        return min_heap[0]