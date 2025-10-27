# https://leetcode.com/problems/maximum-subsequence-score/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
import heapq
                
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        # farthest right n2 seen is always smallest in all possible subseqs
        # therefore, use minheap to ensure k-many n1s accounted for sum, with 
        # priority of popping off smallest n1's seen thus far per constant 
        # minheap size of k 
        n1Sum = 0
        minHeap = [] # 
        res = 0

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1)
             
            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                n1Sum -= n1Pop
        
            if len(minHeap) == k:
                res = max(res, n1Sum * n2) # n2 is next smallest due to sorting

        return res

