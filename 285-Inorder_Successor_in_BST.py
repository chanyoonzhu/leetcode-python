# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        """
        - O(log(n)), -O(n)
        - inorder traversal, then search (use binary search instead)
        
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
        """
        
        """
        - O(log(n))
        """ 
        
        if not root:
            return None
        if root.val > p.val:
            return self.inorderSuccessor(root.left, p) or root # smart!
        else: 
            return self.inorderSuccessor(root.right, p)