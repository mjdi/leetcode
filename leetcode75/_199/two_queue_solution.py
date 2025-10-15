from typing import Optional, List
from leetcode75.dshelper.treenode import TreeNode
from collections import deque                
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def bfs(root):
            if not root:
                return []
            
            result = [root.val]  
            parent_queue = deque([root])
            child_queue = deque([])
        
            while len(parent_queue) > 0 or len(child_queue) > 0:
                if len(parent_queue) == 0:
                    parent_queue = child_queue
                    result.append(parent_queue[0].val)
                    child_queue = deque([])
                    continue

                parent = parent_queue.popleft()
                
                if parent.right:
                    child_queue.append(parent.right)

                if parent.left:
                    child_queue.append(parent.left)
                
            return result 
        
        return bfs(root)
        
