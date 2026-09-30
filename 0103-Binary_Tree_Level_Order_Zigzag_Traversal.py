# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- bfs
- O(n), O(n)
"""
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        is_zig = True
        q1, q2 = deque([root]), deque()
        res = [[]]
        
        while True:
            for node in q1:
                if is_zig:
                    res[-1].append(node.val)
                else:
                    res[-1].insert(0, node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            if not q2:
                return res
            res.append([])
            is_zig = not is_zig
            q1, q2 = q2, deque()