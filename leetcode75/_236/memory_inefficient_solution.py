# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
from leetcode75.dshelper.treenode import TreeNode

# I have no easy way of adding the p and q objects as params for direct object comparison,
# hence in my test I just create a new TreeNode with the same .val

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p = p.val
        self.pfound = False
        self.ppath = []
        self.q = q.val
        self.qfound = False
        self.qpath = []

        self.ancestor_nodes = {}
        
        def dfs1(node, path):
            if self.pfound and self.qfound:
                return 
            if not node:
                return

            path = path + [node.val]
            
            if node.val == self.p:
                self.ppath = path
                self.pfound = True
            if node.val == self.q:
                self.qpath = path
                self.qfound = True
            
            dfs1(node.left, path)   
            dfs1(node.right, path) 
        
        dfs1(root, [])  

        lca = -1
        i = 0 
        while i < len(self.ppath) and i < len(self.qpath):
            ip, iq = self.ppath[i], self.qpath[i]
            if ip == iq:
                lca = ip
            i += 1

        return TreeNode(lca)
