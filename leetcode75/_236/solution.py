from leetcode75.dshelper.treenode import TreeNode

 # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solutions/6911440/beats-100-easiest-explanation-and-code-java-python-c-javascript/?envType=study-plan-v2&envId=leetcode-75
 # 
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case
        if not root or root.val == p.val or root.val == q.val:
            return root
        
        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Case 1: p and q are found in different subtrees
        if left and right:
            return root
        
        # Case 2: both nodes found in one subtree
        return left if left else right