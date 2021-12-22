# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs + hashset (can also use bfs)
- this solution applies to non-BST as well
- O(n), O(n)
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.dfs(root, set(), k)
        
    def dfs(self, node, visited, target):
        if not node:
            return False
        if (target - node.val) in visited:
            return True
        visited.add(node.val)
        if self.dfs(node.left, visited, target):
            return True
        if self.dfs(node.right, visited, target):
            return True
        return False

"""
- dfs (inorder) + two pointers
- O(n), O(n)
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node_list = self.inOrderTraversal(root)
        l, r = 0, len(node_list) - 1
        while l < r:
            if node_list[l] + node_list[r] == k:
                return True
            elif node_list[l] + node_list[r] < k:
                l += 1
            else:
                r -= 1
        return False
        
    def inOrderTraversal(self, node):
        if not node:
            return []
        return self.inOrderTraversal(node.left) + [node.val] + self.inOrderTraversal(node.right)
        
        