# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs + dynamic programming
- O(n), O(n)
"""
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        # return min(self.helper(root))
        return min(self.helper(root)[:2])
        
        
    def helper(self, node):
        if not node:
            return (float('inf'), 0, 0) # min when node empty, min when node has camera
        l_cam_covered, l_covered, l_need_cover = self.helper(node.left)
        r_cam_covered, r_covered, r_need_cover = self.helper(node.right)
        cam_covered = min(l_need_cover, l_covered, l_cam_covered) + min(r_need_cover, r_covered, r_cam_covered) + 1
        covered = min(l_cam_covered + min(r_covered, r_cam_covered), r_cam_covered + min(l_covered, l_cam_covered))
        need_cover = l_covered + r_covered
        return (cam_covered, covered, need_cover) 