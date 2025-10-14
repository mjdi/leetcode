# https://leetcode.com/problems/leaf-similar-trees/submissions/1734181078/?envType=study-plan-v2&envId=leetcode-75
from leetcode75.dshelper.treenode import TreeNode
from typing import Optional

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaves(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            collect_leaves(node.left, leaves)
            collect_leaves(node.right, leaves)
            
        root1_leaves, root2_leaves = [], []
        
        collect_leaves(root1, root1_leaves)
        collect_leaves(root2, root2_leaves)
        
        return root1_leaves == root2_leaves
