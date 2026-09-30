"""
- https://leetcode.com/problems/find-leaves-of-binary-tree/
- summary: use a hashmap to keep the nodes of same height (starting from the bottom), sort hashmap and print (can use an array to optimize)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- Tree traversal (height) + hashmap + sorting
- O(nlogn),O(n)
"""
class Solution:
    def __init__(self):
        self.height_to_vals = defaultdict(list)
        
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self._getHeight(root)
        return [self.height_to_vals[h] for h in sorted(self.height_to_vals)]
    
    def _getHeight(self, node):
        if not node:
            return 0
        height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))
        self.height_to_vals[height].append(node.val)
        return height

"""
- Tree traversal (height) + array
- O(n),O(n)
"""
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, node, res):
        if not node:
            return -1
        l_height = self.dfs(node.left, res)
        r_height = self.dfs(node.right, res)
        height = max(l_height, r_height) + 1
        if len(res) > height:
            res[height].append(node.val)
        else:
            res.append([node.val])
        return height

"""
- Another solution
- Tree traversal (height) + array
- O(n),O(n)
"""
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        
        def dfs(node):
            height = -1
            if node.left:
                height = max(height, dfs(node.left))
            if node.right:
                height = max(height, dfs(node.right))
            height += 1
            if len(res) == height:
                res.append([])
            res[height].append(node.val)
            return height
    
        dfs(root)
        return res