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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        bfs = deque()
        if root: bfs.append((0, root))
            
        while bfs:
            height, node = bfs.popleft()
            if height == len(res):
                res.append(node.val)
            else:
                res[height] = node.val
            if node.left: bfs.append((height + 1, node.left))
            if node.right: bfs.append((height + 1, node.right))
        
        return res
        