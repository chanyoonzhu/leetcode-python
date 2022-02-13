# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- LCA + dfs (recursive)
- MLE
"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        ancestor = self.lowestCommonAncestor(root, startValue, destValue)
        path_start = self.dfs(ancestor, startValue, "")
        path_dest = self.dfs(ancestor, destValue, "")
        return "U" * len(path_start) + path_dest
        
    def dfs(self, root, target, path):
        if not root:
            return ""
        if root.val == target:
            return path
        left_path = self.dfs(root.left, target, path + "L")
        right_path = self.dfs(root.right, target, path + "R")
        return left_path if left_path else right_path
        
        
    def lowestCommonAncestor(self, root, start, end):
        if not root:
            return None
        mid = root.val == start or root.val == end
        if mid:
            return root
        l = self.lowestCommonAncestor(root.left, start, end)
        r = self.lowestCommonAncestor(root.right, start, end)
        if l and r:
            return root
        return l or r

"""
- LCA + dfs (iterative)
"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        ancestor = self.lowestCommonAncestor(root, startValue, destValue)
        return self.dfs(ancestor, startValue, destValue)
        
    def dfs(self, root, start, dest):
        ps = pd = ""
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if node.val == start:
                ps = path
            if node.val == dest:
                pd = path
            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + "R"))
        return "U" * len(ps) + pd
        
        
    def lowestCommonAncestor(self, root, start, end):
        if not root:
            return None
        mid = root.val == start or root.val == end
        if mid:
            return root
        l = self.lowestCommonAncestor(root.left, start, end)
        r = self.lowestCommonAncestor(root.right, start, end)
        if l and r:
            return root
        return l or r
        
        