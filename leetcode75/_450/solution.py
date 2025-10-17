from leetcode75.dshelper.treenode import TreeNode
from typing import Optional
                
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        pred = None # predecessor
        pred_dir = ''
        node = root
        while node:
            if node:
                if node.val == key:
                    break
                elif node.val > key:
                    pred = node
                    if node.left:
                        pred_dir = 'left'
                        node = node.left
                    else:
                        break
                else:
                    pred = node
                    if node.right:
                        pred_dir = 'right'
                        node = node.right
                    else:
                        break
        # case 0: key not found
        if node.val != key:
            return root
        # case 1: no successors
        if node.left is None and node.right is None:
            if pred_dir == 'left':
                pred.left = None
            elif pred_dir == 'right':
                pred.right = None
            else:
                return None # delete root
        # case 2: 1 successor
        elif node.left is None or node.right is None:
            if pred_dir == 'left':
                if node.left:
                    pred.left = node.left
                else:
                    pred.left = node.right
            elif pred_dir == 'right':
                if node.left:
                    pred.right = node.left
                else:
                    pred.right = node.right
            else: # pred_dir = None, key is found at the root
                if node.left:
                    root = node.left
                else:
                    root = node.right
                
        # case 2: 2 successors
        # find smallest value in right subtree or largest value in left subtree
        # and swap the node's val with it, then safely remove the other node
        else:
            # use smallest value in right subtree that is larger than nodes' val                       
            swap_pred = node.right
            swap = swap_pred.left
            if swap:
                while swap:
                    if swap.left:
                        swap_pred = swap
                        swap = swap.left
                    else:
                        node.val = swap.val # set node's val to swap_pred's val
                        swap_pred.left = swap.right
                        break
            else: # node.right is the only value larger
                node.val = swap_pred.val
                node.right = swap_pred.right
             
        return root
