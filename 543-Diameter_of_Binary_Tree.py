# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode') -> 'int':
        
        self.diameter = 0
        
        def helper(root):
            if not root:
                return [-1, -1]
            left = max(helper(root.left))
            right = max(helper(root.right))
            curr = left + right + 2
            self.diameter = max(self.diameter, curr)
            return [left+1, right+1]
        
        self.diameter = 0
        helper(root)
        
        return self.diameter


n1 = TreeNode(1)
n1.left = TreeNode(2)
n1.right = TreeNode(3)
n1.left.left = TreeNode(4)
n1.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(n1))