"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

"""
- dfs (in-order traversal)
- O(n), O(n)
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        def dfs(node):
            if not node:
                return (None, None) # leftmost, rightmost
            l_leftmost, l_rightmost = dfs(node.left)
            r_leftmost, r_rightmost = dfs(node.right)
            if l_rightmost:
                l_rightmost.right = node
                node.left = l_rightmost
            if r_leftmost:
                r_leftmost.left = node
                node.right = r_leftmost
            return (l_leftmost or node, r_rightmost or node)
    
        if not root:
            return None
        leftmost, rightmost = dfs(root)
        rightmost.right = leftmost
        leftmost.left = rightmost
        return leftmost

"""
- dfs (in-order traversal): global variable
- O(n), O(n)
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        def dfs(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal leftmost, rightmost
            if node:
                dfs(node.left)
                if rightmost:
                    rightmost.right = node
                    node.left = rightmost
                else:
                    leftmost = node        
                rightmost = node
                dfs(node.right)
        
        if not root: return None
        leftmost, rightmost = None, None
        dfs(root)
        leftmost.left = rightmost
        rightmost.right = leftmost
        return leftmost

"""
- dfs (in-order traversal): iterative
- O(n), O(n)
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
    
        if not root:
            return None
        stack = []
        node = root
        start = prev = Node(-1)
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            prev.right, node.left, prev = node, prev, node
            node = node.right
            
        start.right.left, prev.right = prev, start.right
        return start.right
