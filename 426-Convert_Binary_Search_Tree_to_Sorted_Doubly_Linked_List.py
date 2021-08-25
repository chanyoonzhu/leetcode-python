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
            if node.left:
                left_leftmost, left_rightmost = dfs(node.left)
                left_rightmost.right = node
                node.left = left_rightmost
            else:
                left_leftmost = node
            if node.right:
                right_leftmost, right_rightmost = dfs(node.right)
                right_leftmost.left = node
                node.right = right_leftmost
            else:
                right_rightmost = node
            return (left_leftmost, right_rightmost)
        
        if not root: return None
        leftmost, rightmost = dfs(root)
        leftmost.left = rightmost
        rightmost.right = leftmost
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
def treeToDoublyList(self, root):
    if not root: return
    dummy = Node(0, None, None)
    prev = dummy
    stack, node = [], root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        node.left, prev.right, prev = prev, node, node
        node = node.right
    dummy.right.left, prev.right = prev, dummy.right
    return dummy.right
