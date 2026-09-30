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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        q = deque()
        q.append((root, 0))
        res = []
        cur_max, cur_height = float("-inf"), 0
        
        while q:
            node, height = q.popleft()
            if height > cur_height:
                res.append(cur_max)
                cur_max, cur_height = node.val, height
            else:
                cur_max = max(cur_max, node.val)
            if node.left:
                q.append((node.left, height + 1))
            if node.right:
                q.append((node.right, height + 1))
        res.append(cur_max) # easy to miss
        return res