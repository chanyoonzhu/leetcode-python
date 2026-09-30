# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- binary search
- O(logn*logn)
"""
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_depth = 0
        node = root
        while node:
            max_depth += 1
            node = node.left
        
        if max_depth == 1:
            return 1
                
        def binary_search(node, depth):
            l, r = 0, 2 ** (depth - 1) # positions of leaf nodes
            while l < r:
                mid = l + (r - l) // 2
                if is_middle_full(node, depth):
                    l = mid + 1
                    node = node.right
                else:
                    r = mid
                    node = node.left
                depth -= 1
            return l
        
        def is_middle_full(node, depth):
            if not node:
                return depth == 0
            if not node.right:
                return depth == 1
            ptr, depth = node.right, depth - 1
            while ptr:
                ptr = ptr.left
                depth -= 1
            return depth == 0
        
        last_full_index = binary_search(root, max_depth)
        return 2 ** (max_depth - 1) - 1 + last_full_index
        
        """
        - divide and conquer
        - log(n)*log(n)
        """
        
        
        def leftHeight(root):
            if not root:
                return 0
            return 1 + leftHeight(root.left)
        
        def rightHeight(root):
            if not root:
                return 0
            return 1 + rightHeight(root.right)
        
        left_h = leftHeight(root)
        right_h = rightHeight(root)
        if left_h == right_h:
            return 2 ** (left_h) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

"""
- binary search
- O(logn*logn)
"""
class Solution2:
        # @param {TreeNode} root
        # @return {integer}
        def countNodes(self, root):
            if not root:
                return 0
            leftDepth = self.getDepth(root.left)
            rightDepth = self.getDepth(root.right)
            if leftDepth == rightDepth:
                return pow(2, leftDepth) + self.countNodes(root.right) # number of nodes of root and left tree.
            else: 
                return pow(2, rightDepth) + self.countNodes(root.left) # number of nodes of root and right tree.
    
        def getDepth(self, root):
            if not root:
                return 0
            return 1 + self.getDepth(root.left)

"""
- binary search
- O(logn*logn)
"""
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth = self.getDepth(root)
        last_node_idx = self.binarySearch(root, depth)
        return 2 ** (depth - 1) + last_node_idx
        
    def existInLastRow(self, idx, root, depth):
        node = root
        for i in range(depth-2, -1, -1):
            if idx & (1 << i):
                node = node.right
            else:
                node = node.left
        return node != None
        
    def binarySearch(self, node, depth):
        last_row_count = 2 ** (depth - 1)
        lo, hi = 0, last_row_count - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if self.existInLastRow(mid, node, depth):
                lo = mid
            else:
                hi = mid - 1
        return lo
    
    def getDepth(self, node):
        if not node:
            return 0
        return 1 + self.getDepth(node.left)

            