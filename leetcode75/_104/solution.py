# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
from leetcode75.dshelper.treenode import TreeNode
from typing import Optional 

class Solution:
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        def descend(depth, parent):
            curr_depth = depth
            if parent.left:
                depth = descend(curr_depth+1, parent.left)
            if parent.right:
                depth = max(depth,descend(curr_depth+1,parent.right))
            return depth
        maxd = 1
        if root:
            return descend(1,root)
        else:
            return 0

