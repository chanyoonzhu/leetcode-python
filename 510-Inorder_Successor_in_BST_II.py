"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

"""
- BST
- O(H)
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if not node:
            return None
        if node.right: # if has right node, successor is the leftmost child of its right node (or the right node itself if no left sub)
            node = node.right
            while node.left:
                node = node.left
            return node
        # if no right node, successor is the first parent greater than itself
        parent = node.parent
        while parent:
            if parent.val > node.val:
                return parent
            parent = parent.parent
        return None
        