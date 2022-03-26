# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        """
        dfs - pre-order traversal
        - O(nlogn): O(n) for traversal, O(nlogn) for search, O(n) for extracting result
        - O(n): O(n) for traversal, O(n) stacks for completely skewed tree, O(n) for extracting result
        """
        lst = []
        
        def dfs(x, y, node):
            if not node: return
            lst.append((x, y, node.val))
            dfs(x-1, y+1, node.left)
            dfs(x+1, y+1, node.right)
            
        dfs(0, 0, root)
        lst.sort()
        res = []
        prev_x = None
        for x, y, val in lst:
            if x == prev_x:
                res[-1].append(val)
            else:
                res.append([val])
            prev_x = x
        return res

"""
bfs
- O(nlogn): O(n) for traversal, O(nlogn) for search, O(n) for extracting result
- O(n): O(n) for traversal, O(n) -  At any given moment, the queue contains no more than two levels of nodes in the tree. The maximal number of nodes at one level is n/2 , which is the number of the leaf nodes in a balanced binary tree, O(n) for extracting result
"""
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_to_vals = defaultdict(list)
        q = deque([(root, 0, 0)]) # node, row, col
        while q:
            node, row, col = q.popleft()
            col_to_vals[col].append((row, node.val)) # later sort by row, then node.val
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        
        for col in col_to_vals:
            col_to_vals[col] = sorted(col_to_vals[col])
            
        return [[val for _, val in col_to_vals[col]] for col in sorted(col_to_vals)]