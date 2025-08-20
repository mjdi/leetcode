# https://leetcode.com/problems/leaf-similar-trees/submissions/1734181078/?envType=study-plan-v2&envId=leetcode-75
from leetcode75.dshelper.treenode import TreeNode
from typing import Optional

class Solution:
    @staticmethod
    def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def extend_lvs(lvs, parent):
            if not parent.left and not parent.right:
                return [parent.val]
            if parent.left:
                lvs.extend(extend_lvs([], parent.left))
            if parent.right:
                lvs.extend(extend_lvs([], parent.right))
            return lvs
        
        return extend_lvs([],root1) == extend_lvs([],root2)