from leetcode75.dshelper.treenode import TreeNode
from typing import Optional
class Solution:
    @staticmethod
    def goodNodes(root: TreeNode) -> int:
        maxval = root.val
        num_good_nodes = 1 # always one which is the root
       
        def accum_good_nodes(parent, num_good_nodes, maxval):
            if parent.val >= maxval:
                num_good_nodes += 1
            maxval = max(parent.val, maxval)
            if not parent.left and not parent.right:
                return num_good_nodes
            num_good_nodes += accum_good_nodes(parent.left, num_good_nodes, maxval)
            num_good_nodes += accum_good_nodes(parent.right, num_good_nodes, maxval)
            print(f'{parent.val=}, {num_good_nodes=}')
            return num_good_nodes

        return accum_good_nodes(root, num_good_nodes, maxval)