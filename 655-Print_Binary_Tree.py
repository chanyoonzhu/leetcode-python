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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        M = self.getHeight(root)
        N = 2 ** M - 1
        res = [[""] * N for _ in range(M)]
        self.dfs(root, 0, 0, N-1, res)
        return res
        
    def dfs(self, node, row, col_start, col_end, printed):
        if not node:
            return
        col = (col_start + col_end) // 2
        printed[row][col] = str(node.val)
        row += 1
        self.dfs(node.left, row, col_start, col - 1, printed)
        self.dfs(node.right, row, col + 1, col_end, printed)
        
    
    # 1-based height
    def getHeight(self, node):
        if not node:
            return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))