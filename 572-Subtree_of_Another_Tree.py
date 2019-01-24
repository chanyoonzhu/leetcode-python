# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def isSameTree(s, t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            if s.val == t.val:
                return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
            
        if not s and not t: 
            return True
        elif s and t:
            if s.val == t.val:
                if isSameTree(s, t):
                    return True
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return False
                
                
                
        