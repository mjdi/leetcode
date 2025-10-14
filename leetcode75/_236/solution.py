# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
from leetcode75.dshelper.treenode import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p and q might be ints not Treenodes, look into this
        return TreeNode()