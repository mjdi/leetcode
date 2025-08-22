# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75
from leetcode75.dshelper.treenode import TreeNode
from typing import Optional

class Solution:
    @staticmethod
    def longestZigZig(root: Optional[TreeNode]) -> int:
        return 0