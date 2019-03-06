# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        """
        - O(n)
        - binary tree nodes general solution
        
        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        """
        
        """
        - log(n)*log(n)
        - binary search leaf nodes
        
        if not root:
            return 0
        
        height = 0
        ptr = root
        while ptr:
            height += 1
            ptr = ptr.left
            
        def helper(root, pos, level, height):
            if level == height:
                return pos
            else: 
                currLevel = level
                node, prev = root.right, root
                while node:
                    currLevel += 1
                    prev, node = prev, node.left
                if currLevel == height: # still full
                    return helper(root.right, pos*2+1, level+1, height)
                else:
                    return helper(root.left, pos*2, level+1, height)
                
        return (2 ** (height - 1) - 1) + (helper(root, 0, 1, height) + 1)
        """
        
        """
        - divide and conquer
        - log(n)*log(n)
        """
        
        
        def leftHeight(root):
            if not root:
                return 0
            return 1 + leftHeight(root.left)
        
        def rightHeight(root):
            if not root:
                return 0
            return 1 + rightHeight(root.right)
        
        left_h = leftHeight(root)
        right_h = rightHeight(root)
        if left_h == right_h:
            return 2 ** (left_h) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            