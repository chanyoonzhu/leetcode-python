# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs
- O()?
"""
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @lru_cache(None)
        def generate_tree(lo, hi):
            if lo > hi:
                return [None]
            
            all_trees = []
            for x in range(lo, hi + 1):
                left_trees = generate_tree(lo, x - 1)
                right_trees = generate_tree(x + 1, hi)
                
                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(x, l, r)
                        all_trees.append(node)
            return all_trees
                        
        if n == 0: return []
        return generate_tree(1, n)
            
        