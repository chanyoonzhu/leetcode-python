# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    - dfs: return (distance, has_both_found)
    - O(n), O(n)
    """
    def findDistance(self, root, p, q: int) -> int:
        
        def dfs(node, p, q):
            if not node:
                return (0, False)
            
            left, l_found_both = dfs(node.left, p, q)
            right, r_found_both = dfs(node.right, p, q)
            
            if l_found_both:
                return (left, True)
            if r_found_both:
                return (right, True)
            
            if left and right:
                return (left + right + 2, True)
            
            curr = 0
            if node.val == p:
                curr += 1
            if node.val == q:
                curr += 1
                
            if left:
                return (curr + left + 1, curr and left)
                
            if right:
                return (curr + right + 1, curr and right)
            
            return (curr, curr == 2)
        
        return dfs(root, p, q)[0] - 2