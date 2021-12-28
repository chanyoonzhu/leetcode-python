"""
- bst
- O(log(n))
""" 
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        if not root:
            return None
        if root.val > p.val:
            closer_successor = self.inorderSuccessor(root.left, p)
            return closer_successor if closer_successor else root
            """ or 
            return self.inorderSuccessor(root.left, p) or root
            """
        else:
            return self.inorderSuccessor(root.right, p)

"""
- inorder traversal
- O(log(n)), -O(n)
- inorder traversal, then search (use binary search instead)
"""
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        
        inorder = self.inorder(root)
        for i in range(len(inorder)):
            if inorder[i].val == p.val and i != len(inorder)-1:
                return inorder[i+1] 
        return None
        
    def inorder(self, root):
        if not root:
            return []
        res = []
        if root.left:
            res.extend(self.inorder(root.left))
        res.append(root)
        if root.right:
            res.extend(self.inorder(root.right))
        return res