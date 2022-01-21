"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
- bfs
- O(n), O(n)
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        level = []
        level.append(root)
        
        new_level = []
        while level:
            while level:
                node = level.pop(0)
                if level:
                    node.next = level[0]
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level, new_level = new_level, []
        
        return root

"""
- use already connected link
- O(n), O(1)
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node: # node: current parent
            curr = dummy = Node() # curr: traverse each level dummy: dummy head of each level
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next
               
        return root
        
        