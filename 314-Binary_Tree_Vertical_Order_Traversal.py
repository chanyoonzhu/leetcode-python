# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs
- wrong answer: node on the left tree always printed first (higher level should be printed first)
"""
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_to_val = defaultdict(list)
        self.dfs(root, 0, level_to_val)
        return [level_to_val[level] for level in sorted(level_to_val)]
        
        
    def dfs(self, node, level, level_to_val):
        if not node: return
        level_to_val[level].append(node.val)
        self.dfs(node.left, level-1, level_to_val)
        self.dfs(node.right, level+1, level_to_val)


"""
- dfs
- add height for sorting
"""
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_to_val = defaultdict(list)
        self.dfs(root, 0, 0, level_to_val)
        res = []
        for level in sorted(level_to_val):
            res.append([value for height, value in sorted(level_to_val[level], key=lambda x: x[0])]) # easy to miss: only order by first element, keep the order of the second element (already sorted by left/right node)
        return res
        
        
    def dfs(self, node, height, level, level_to_val):
        if not node: return
        level_to_val[level].append((height, node.val))
        self.dfs(node.left, height + 1, level-1, level_to_val)
        self.dfs(node.right, height + 1, level+1, level_to_val)


"""
- bfs (best choice)
- O(n), O(n)
"""
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_to_vals = defaultdict(list)
        bfs = deque()
        if root: bfs.append((0, root)) # level, node
        
        while bfs:
            level, node = bfs.popleft()
            level_to_vals[level].append(node.val)
            if node.left: bfs.append((level - 1, node.left))
            if node.right: bfs.append((level + 1, node.right))
        
        return [level_to_vals[level] for level in sorted(level_to_vals)]  