# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs + hashing
- caveat: # need to use either pre/post-order, inorder won't work since two different tree can have the same serialized string
- O(n), O(n)
"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = set()
        in_result = set()
        result = []
        
        def dfs(node):
            if not node: return ""
            ser = f"{node.val},{dfs(node.left)},{dfs(node.right)}"
            if ser in subtrees and ser not in in_result:
                result.append(node)
                in_result.add(ser)
            subtrees.add(ser)
            return ser
        
        dfs(root)
        return list(result)

"""
- class method
"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        serialized = set()
        in_result = set()
        res = []
        self.dfs(serialized, in_result, res, root)
        return res
        
    def dfs(self, serialized, in_result, res, node):
        if not node:
            return ""
        ser = f"{str(node.val)}#{self.dfs(serialized, in_result, res, node.left)}#{self.dfs(serialized, in_result, res, node.right)}"
        if ser not in serialized:
            serialized.add(ser)
        elif ser not in in_result:
            in_result.add(ser)
            res.append(node)
        return ser