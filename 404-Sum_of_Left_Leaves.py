# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # sumOfLL = 0
        # if root and root.left:
        #     if not root.left.left and not root.left.right:
        #         sumOfLL += root.left.val
        #     else:
        #         sumOfLL += self.sumOfLeftLeaves(root.left)
        # if root and root.right:
        #     sumOfLL += self.sumOfLeftLeaves(root.right)
        # return sumOfLL
        
        """
        a better solution, conditions combined
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)