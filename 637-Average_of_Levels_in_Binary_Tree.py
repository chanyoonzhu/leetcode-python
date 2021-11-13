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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res = []
        q = deque()
        q.append((root, 0))
        cur_level = 0
        sum_, count = root.val, 1
        
        while q:
            node, level = q.popleft()
            if level > cur_level:
                res.append(sum_ / count)
                cur_level = level
                sum_, count = node.val, 1
            else:
                sum_ += node.val 
                count += 1
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        res.append(sum_ / count) # easy to miss
        return res

"""
- dfs
- O(n), O(n)
"""
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        sum_and_count = list()
        
        def dfs(node, level):
            if not node:
                return
            if level >= len(sum_and_count):
                sum_and_count.append([node.val, 1])
            else:
                sum_, count = sum_and_count[level] 
                sum_and_count[level] = [sum_ + node.val, count + 1]
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        
        return [sum_ / count for sum_, count in sum_and_count]
        