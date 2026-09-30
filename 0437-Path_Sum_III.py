# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- prefix sum with hashmap
- O(n), O(n)
- similar problem: 560
"""
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        def dfs(node, curr_sum):
            if not node:
                return
            
            curr_sum += node.val
                
            self.result += count_map[curr_sum - targetSum]
            
            count_map[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            count_map[curr_sum] -= 1
                
        self.result = 0
        count_map = collections.defaultdict(int)
        count_map[0] = 1
        dfs(root, 0)
        return self.result
        