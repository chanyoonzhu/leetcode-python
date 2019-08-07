"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        """
        # level traversal
        
        if not root:
            return None
        traverse = [[root]]
        root.next = None
        while traverse[-1][0].left:
            level = []
            for node in traverse[-1]:
                if level: level[-1].next = node.left
                node.left.next = node.right
                node.right.next = None
                level.extend([node.left, node.right])
            traverse.append(level)
                
        return root
        """
        
        """
        # make use of preconnected nodes - clever
        if not root:
            return None
        prev, curr = root, None
        while prev.left:
            curr = prev
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            prev = prev.left
        """
        
        if not root:
            return None
        self.helper(root.left, root.right)
        return root
    
    def helper(self, left, right):
        if not left:
            return None
        left.next = right 
        self.helper(left.left, left.right)
        self.helper(left.right, right.left)
        self.helper(right.left, right.right)