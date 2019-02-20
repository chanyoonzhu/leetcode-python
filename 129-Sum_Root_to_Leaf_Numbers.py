# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        - dfs
        - better solution: https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/41383/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively).
        """
        def dfs(root, n):
            if not root: return n
            n = n * 10 + root.val
            if not root.left and not root.right:
                return n
            elif root.left and root.right:
                return dfs(root.left, n) + dfs(root.right, n)
            elif root.left:
                return dfs(root.left, n)
            else:
                return dfs(root.right, n)
            
        return dfs(root, 0)

        """
        - redo
        """

        def sumNumbers(self, root: 'TreeNode') -> 'int':
        
            def helper(root, num, sum_):
                if not root:
                    return sum_
                num = num * 10 + root.val
                if not root.left and not root.right:
                    sum_ += num
                    return sum_
                return helper(root.left, num, sum_) + helper(root.right, num, sum_)
    
            return helper(root, 0, 0)