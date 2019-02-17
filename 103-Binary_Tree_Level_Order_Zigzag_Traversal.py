# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = [[]]
        
        q = [(root, 0)]
        
        currLevel = 0
        while q:
            node, level = q.pop(0)
            if currLevel != level:
                res.append([])
                currLevel = level
            if level % 2 == 0: 
                res[-1].append(node.val)
            else:
                res[-1].insert(0, node.val)
            left = node.left
            right = node.right
            level += 1
            if left: q.append((left, level))
            if right: q.append((right, level))
                
        return res