# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional, List
from leetcode75.dshelper.treenode import TreeNode
from collections import deque                
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            if not root:
                return []
            out = []  
            q = deque([root])
            while q:
                qlen = len(q)
                for idx in range(qlen):
                    node = q.popleft()
                    if idx == 0:
                        out.append(node.val)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
            return out
        return bfs(root)
        
