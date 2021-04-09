# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- dfs (preorder)
- O(n), O(n)
"""
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        self.result = []
        self.i = 0 # one variable can use across the whole recursion, smart!
        
        def dfs(node):
            if not node or self.i >= n:
                return
            if node.val != voyage[self.i]:
                self.result = [-1]
                return
            self.i += 1
            if node.left and node.left.val != voyage[self.i]:
                self.result.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
                
                        
        n = len(voyage)
        self.result = []
        dfs(root)
        if self.result and self.result[0] == -1:
            return [-1]
        return self.result