# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs
- O(n), (n)
"""
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []

        def dfs(node, is_root):
            if not node: return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                result.append(node)
            node.left = dfs(node.left, root_deleted) # is parent deleted == is child a new root node
            node.right = dfs(node.right, root_deleted)
            return None if root_deleted else node
        
        dfs(root, True)
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- bfs
- O(n), (n)
"""
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root: return []
        
        to_delete_set = set(to_delete)
        result = []

        q = [(root, True)]
        while q:
            node, is_root = q.pop(0)
            is_to_delete = node.val in to_delete_set
            if is_root and not is_to_delete:
                result.append(node)
            if node.left: 
                q.append((node.left, is_to_delete))
                if node.left.val in to_delete_set: node.left = None
            if node.right: 
                q.append((node.right, is_to_delete))
                if node.right.val in to_delete_set: node.right = None
        return result