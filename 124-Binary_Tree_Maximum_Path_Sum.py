# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        - recursion
        - http://www.cnblogs.com/grandyang/p/4280120.html
        """
        
        return max(self.helper(root))
        
    def helper(self, root):
        
        if not root:
            return (0, 0)
        
        leftHalfMax, leftMax = self.helper(root.left)
        
        rightHalfMax, rightMax = self.helper(root.right)
            
        halfMax = max(root.val + leftHalfMax, root.val + rightHalfMax, root.val) # incase needs to connect to root's parent, can only choose either connecting to the left/right of its child
        fullMax = max(leftHalfMax + root.val + rightHalfMax, halfMax) # in case does not need to connect parent, largest sum path already appeared
        if root.left: fullMax = max(leftMax, fullMax) # don't include leftMax when left is None
        if root.right: fullMax = max(rightMax, fullMax)
        
        return (halfMax, fullMax)

n1 = TreeNode(-2)
n1.left = TreeNode(6)
# n1.right = TreeNode(20)
n1.left.left = TreeNode(0)
n1.left.right = TreeNode(-6)

print(Solution().maxPathSum(n1))