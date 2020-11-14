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
        lst = []            
        queue = deque[(0, 0, root)]
        while queue:
            x, y, node = queue.popleft()
            lst.append((x, y, node.val))
            if node.left:
                queue.append((x-1, y+1, node.left))
            if node.right:
                queue.append((x+1, y+1, node.right))
            
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