# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- bfs
- O(n), O(n)
"""
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
                
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if not node:
                break
            queue.append(node.left)
            queue.append(node.right)
        return not any(queue) # all in queue should be None
        