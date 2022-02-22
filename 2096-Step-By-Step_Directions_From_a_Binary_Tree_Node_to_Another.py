# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- LCA + dfs (recursive)
- TLE
"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        ancestor = self.lowestCommonAncestor(root, startValue, destValue)
        l_path = "U" * len(self.dfs(ancestor, startValue, ""))
        r_path = self.dfs(ancestor, destValue, "")
        return l_path + r_path
        
        
    def dfs(self, root, target, path):
        if not root:
            return None
        if root.val == target:
            return path
        return self.dfs(root.left, target, path + "L") or self.dfs(root.right, target, path + "R")
                
        
    def lowestCommonAncestor(self, root, start, dest):
        if not root:
            return None
        if root.val == start or root.val == dest:
            return root
        l = self.lowestCommonAncestor(root.left, start, dest)
        r = self.lowestCommonAncestor(root.right, start, dest)
        if l and r:
            return root
        return l or r

"""
- LCA + dfs (iterative)
"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        ancestor = self.lowestCommonAncestor(root, startValue, destValue)
        stack = [(ancestor, "")]
        l_path = r_path = ""
        while stack:
            node, path = stack.pop()
            if node.val == startValue:
                l_path = "U" * len(path)
            elif node.val == destValue:
                r_path = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
        return l_path + r_path     
        
    def lowestCommonAncestor(self, root, start, dest):
        if not root:
            return None
        if root.val == start or root.val == dest:
            return root
        l = self.lowestCommonAncestor(root.left, start, dest)
        r = self.lowestCommonAncestor(root.right, start, dest)
        if l and r:
            return root
        return l or r
        
        