# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75
from leetcode75.dshelper.treenode import TreeNode
from typing import Optional

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxzz = 0
        def dfs(node, dir, lenzz):
            if not node:
                return
            self.maxzz = max(self.maxzz, lenzz)    
            dfs(node.left, 'L', (lenzz if dir == 'R' or dir == 'B' else 0) + 1) 
            dfs(node.right,'R', (lenzz if dir == 'L' or dir == 'B' else 0) + 1) 
        dfs(root, 'B', 0)    
        return self.maxzz