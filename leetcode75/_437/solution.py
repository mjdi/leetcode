# https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75
from collections import defaultdict
from leetcode75.dshelper.treenode import TreeNode
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1
        
        def dfs(node, root_sum):
            if not node:
                return
            root_sum += node.val
            self.total += self.lookup[root_sum] 
            self.lookup[root_sum + targetSum] += 1
            dfs(node.left, root_sum)
            dfs(node.right, root_sum)
            self.lookup[root_sum + targetSum] -= 1

        # def helper(node,cur):
        #     if not node:
        #         return
        #     helper(node.left,cur+node.val)
        #     helper(node.right,cur+node.val)
        #     if cur + node.val == targetSum:
        #         self.total += 1
            
        # def dfs(node):
        #     if not node:
        #         return
        #     helper(node,0)
        #     dfs(node.left)
        #     dfs(node.right)
            
        # dfs(root)
        dfs(root,0)
        
        return self.total