# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        """
        - Questions:What if 2 value has equal length to the target?
        
         def search(root, minInfo, target):
        
            if not root:
                return minInfo

            rootInfo = (root.val - target, root)
            if abs(rootInfo[0]) < abs(minInfo[0]):
                    minInfo = rootInfo
                    
            if root.val == target:
                return rootInfo
            elif root.val > target:
                return search(root.left, minInfo, target)
            elif root.val < target:
                return search(root.right, minInfo, target)
        
        return search(root, (float("inf"), None), target)[1].val
        """

        rootVal = root.val
        nextRoot = root.left if rootVal > target else root.right
        if not nextRoot: return rootVal
        nextVal = self.closestValue(nextRoot, target)
        if abs(rootVal - target) < abs(nextVal - target):
            return rootVal
        else:
            return nextVal