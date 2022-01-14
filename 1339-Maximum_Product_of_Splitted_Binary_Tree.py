# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs (with array)
- O(n), O(n)
"""
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        res = 0
        self.dfs(root, sums)
        for x in sums[:-1]:
            y = sums[-1] - x
            res = max(res, x * y)
            
        return res % (10 ** 9 + 7)
        
    def dfs(self, node, sums):
        if not node:
            return 0
        sums.append(node.val + self.dfs(node.left, sums) + self.dfs(node.right, sums))
        return sums[-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- dfs
- O(n), O(h)
"""
class Solution:
    
    def __init__(self):
        self.res = 0
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = self.dfs(root)
        self.dfs(root, total_sum)
            
        return self.res % (10 ** 9 + 7)
        
    def dfs(self, node, total_sum=None):
        if not node:
            return 0
        cur_sum = node.val + self.dfs(node.left, total_sum) + self.dfs(node.right, total_sum)
        if total_sum:
            self.res = max(self.res, (total_sum - cur_sum) * cur_sum)
        return cur_sum
        