"""
- dfs
- O(n), O(n)
"""
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            
            return [rob, not_rob]
        
        return max(dfs(root))

"""
- bfs
- similar questions: 198, 213 House Robber series
"""