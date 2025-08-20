# Definition for a binary tree node.
from typing import List, Optional
import pprint as pp

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_binary_tree(nodes: Optional[List]) -> Optional[TreeNode]:
    if len(nodes) == 0:
        return None
    
    root = TreeNode(nodes.pop(0))
    level_nodes = [root]
    
    level = 1
    while nodes:
        new_level_nodes = []
    
        pow2 = 2 ** (level)
        node_vals = nodes[0:pow2]
        nodes = nodes[pow2:]
    
        for i in range(0, len(level_nodes)):
            if (i * 2) < len(node_vals) and node_vals[i * 2] is not None:
                left = TreeNode(node_vals[i * 2])
                level_nodes[i].left = left 
                new_level_nodes.append(left)
            else:
                level_nodes[i].left = None
                new_level_nodes.append(None)
            
            if (i * 2 + 1) < len(node_vals) and node_vals[i * 2 + 1] is not None:
                right = TreeNode(node_vals[i * 2 + 1])
                level_nodes[i].right = right 
                new_level_nodes.append(right)
            else:
                level_nodes[i].right = None
                new_level_nodes.append(None)

        level_nodes = new_level_nodes
        level += 1

    return root


def write_binary_tree(root: TreeNode) -> str:
    out_levels = []
    branches = []
    out_levels.append(f'             {root.val:03d}')
    level = 0
    branches.append('        /              \\') 
    prev_level_nodes = [root.left, root.right]
    if root.left is not None and root.right is not None:
        out_levels.append(f'    {root.left.val:03d}             {root.right.val:03d}')
    elif root.left is not None:
        out_levels.append(f'    {root.left.val:03d}             ___')
    elif root.right is not None:
        out_levels.append(f'    ___             {root.right.val:03d}')
    else:
        out_levels.append(f'    ___             ___')

    level = 1
    branches.append('   /      \\         /     \\') 
    children_in_next_level = [bool(root.left), bool(root.right)]  
    while any(children_in_next_level):

        dont_add_last_branches = False
        children_in_next_level = []
        level_nodes = []
        level += 1
        out_levels.append('')

        for node in prev_level_nodes:
            if node is not None:
                level_nodes.append(node.left)
                children_in_next_level.append(bool(node.left)) 
                level_nodes.append(node.right)
                children_in_next_level.append(bool(node.right))
                
                if node.left:
                    left_val = '__' if not node.left.val else node.left.val
                    if left_val == '__':
                        out_levels[level] += left_val
                    else:
                        out_levels[level] += f'{left_val:03d}'
                else:
                    out_levels[level] += '  '
                out_levels[level] += '      '    
                if node.right:
                    right_val = '__' if not node.right.val else node.right.val
                    if right_val == '__':
                        out_levels[level] += right_val
                    else:
                        out_levels[level] += f'{right_val:03d}'
                else:
                    out_levels[level] += '  '
                out_levels[level] += '      '
            else:
                level_nodes.append(None)
                level_nodes.append(None)
                children_in_next_level.append(False) 
                children_in_next_level.append(False) 
                
        prev_level_nodes = level_nodes 

        # add padding on each side as the level increases
        if any(children_in_next_level):
            branches.append((2 ** (level)) * (' /  ' + (2**(level-1)) * ' ' + '\\ '))
            for i in range(0,len(out_levels)):
                branches[i] = (2**(level)) * ' ' + branches[i] 

        for i in range(0,len(out_levels)):
            out_levels[i] = (2**(level-1)) * ' ' + out_levels[i] 

    out = '\n'
    for out_level, branch in zip(out_levels, branches):
        out = out + out_level + '\n' + branch + '\n'

    return out
