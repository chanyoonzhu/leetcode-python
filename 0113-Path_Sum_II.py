# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        """
        - dfs with stack
        
        def dfs(root, path, sum_):
            if not root:
                return
            stack = [root]
            while root.left:
                stack.append(root.left)
                root = root.left
            path += [n.val for n in stack]
            if not root.right and sum(path) == sum_:
                    paths.append(path[:]) # df: need a deep copy since path is going to change
            while stack:
                dfs(stack[-1].right, path, sum_)
                stack.pop()
                path.pop()
                
        paths = []
        dfs(root, [], sum_)
        return paths
        """
        
        """
        - dfs recursive
        """
    
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls+[root.val], res)
                
            
            

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(13)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(2)
n9 = TreeNode(5)
n10 = TreeNode(1)
n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.left = n9
n6.right = n10

sl = Solution()
print(sl.pathSum(n1, 22))

