# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- caveat: node values are not unique
- dfs
- O(n*s) s - number of nodes in subroot
"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, node, other_node):
        if not node and not other_node:
            return True
        if not node or not other_node:
            return False
        if node.val != other_node.val:
            return False
        return self.isSameTree(node.left, other_node.left) and self.isSameTree(node.right, other_node.right)

"""
- caveat: node values are not unique
- dfs
- O(|n|+|s|)
"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        sers = set()
        
        def serialize(node, cache=None):
            if not node:
                return " "
            ser = f"{node.val}#{serialize(node.left, cache)}#{serialize(node.right, cache)}"
            if cache != None:
                cache.add(ser) # optimizing: can hash ser to save space
            return ser
        
        serialize(root, sers)
        return serialize(subRoot) in sers
        
                
                
                
        