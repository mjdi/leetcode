# Definition for a binary tree node.
from typing import List, Optional
import pprint as pp

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_binary_tree(nodes: Optional[List]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if current:
            if i < len(nodes) and nodes[i] is not None:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)
            i += 1
        else:
            continue
        
    return root


def write_binary_tree(root: TreeNode) -> str:
    out_levels = []
    branches = []
    out_levels.append(f'             {root.val:03d}')
    level = 0
    branches.append('        /              \\') 
    prev_parent_nodes = [root.left, root.right]
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
        parent_nodes = []
        level += 1
        out_levels.append('')

        for node in prev_parent_nodes:
            if node is not None:
                parent_nodes.append(node.left)
                children_in_next_level.append(bool(node.left)) 
                parent_nodes.append(node.right)
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
                parent_nodes.append(None)
                parent_nodes.append(None)
                children_in_next_level.append(False) 
                children_in_next_level.append(False) 
                
        prev_parent_nodes = parent_nodes 

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
