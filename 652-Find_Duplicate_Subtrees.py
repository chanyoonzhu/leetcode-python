# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs + hashing
- O(n), O(n)
"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = set()
        in_result = set()
        result = []
        
        def dfs(node):
            if not node: return " " # easy to miss: do not use "", need to mark the leaf node
            ser = f"{node.val},{dfs(node.left)},{dfs(node.right)}"
            if ser in subtrees and ser not in in_result:
                result.append(node)
                in_result.add(ser)
            subtrees.add(ser)
            return ser
        
        dfs(root)
        return list(result)