# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
from leetcode75.dshelper.treenode import TreeNode
from typing import Optional
from collections import deque
                
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        mx = float('-inf')
        ans, lvl = 1, 1
        q = [root]
        while q:
            sum = 0
            nq = []
            for n in q:
                sum += n.val
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            if sum > mx:
                mx = sum
                ans = lvl 
            q = nq 
            lvl += 1                 
        return ans