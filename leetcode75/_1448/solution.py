from leetcode75.dshelper.treenode import TreeNode
from typing import Optional
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def accum(parent, gncnt, maxval):
            if parent.val >= maxval:
                gncnt += 1
                maxval = parent.val
            if parent.left:
                gncnt += accum(parent.left, 0, maxval)
            if parent.right:
                gncnt += accum(parent.right, 0, maxval)
            return gncnt
        return accum(root, 0, root.val)
