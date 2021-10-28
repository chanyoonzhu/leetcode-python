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
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        self.heights = defaultdict(list)
        self.find_height(root, self.heights)
        return [self.heights[h] for h in sorted(self.heights)]
        
        
    def find_height(self, node, heights):
        if not node: 
            return -1
        height = 1 + max(self.find_height(node.left, heights), self.find_height(node.right, heights))
        heights[height].append(node.val)
        return height

"""
- Tree traversal (height) + array
- O(n),O(n)
"""
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        self.heights = []
        self.find_height(root, self.heights)
        return self.heights
        
        
    def find_height(self, node, heights):
        if not node: 
            return -1
        height = 1 + max(self.find_height(node.left, heights), self.find_height(node.right, heights))
        if height >= len(heights):
            heights.append([node.val])
        else:
            heights[height].append(node.val)
        return height