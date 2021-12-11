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
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        M = self.getHeight(root)
        N = 2 ** M - 1
        res = [[""] * N for _ in range(M)]
        self.dfs(root, 0, N // 2, res)
        return res
        
    # an easier-to-understand solution: https://leetcode.com/problems/print-binary-tree/discuss/106240/Python-recursive-solution-easy-to-understand
    def dfs(self, node, row, col, printed):
        if not node:
            return
        printed[row][col] = str(node.val)
        row += 1
        dist_to_parent = 2 ** (len(printed) - row - 1)
        self.dfs(node.left, row, col - dist_to_parent, printed)
        self.dfs(node.right, row, col + dist_to_parent, printed)
        
    
    # 1-based height
    def getHeight(self, node):
        if not node:
            return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))