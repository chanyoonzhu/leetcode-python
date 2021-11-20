# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs
- O(n), O(n)
"""
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []
        self.dfs(sums, root, 0)
        max_ = float("-inf")
        res = -1
        for i, sum_ in enumerate(sums, 1):
            if sum_ > max_:
                res = i
                max_ = sum_
        return res
            
        
    def dfs(self, sums, node: Optional[TreeNode], level: int) -> None:
        if not node:
            return
        if level == len(sums): # use hashmap (defaultdict(int)) to avoid boundary checking
            sums.append(node.val)
        else:
            sums[level] += node.val
        self.dfs(sums, node.left, level + 1)
        self.dfs(sums, node.right, level + 1)

"""
- todo: bfs
"""
        