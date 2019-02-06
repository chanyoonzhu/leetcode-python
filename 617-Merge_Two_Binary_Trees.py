# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        mergedNode = None
        if not t1 and not t2:
            return mergedNode
        elif not t1:
            mergedNode = t2
        elif not t2:
            mergedNode = t1
        else:
            t2.val = t1.val + t2.val
            mergedNode = t2
            mergedNode.left = self.mergeTrees(t1.left, t2.left)
            mergedNode.right = self.mergeTrees(t1.right, t2.right)
        
        return mergedNode