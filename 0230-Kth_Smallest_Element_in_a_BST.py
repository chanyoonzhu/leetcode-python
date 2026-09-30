# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Follow-up question:
Q: What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
A: Combine the BST with a double linked list, with each node in BST having an extra pointer to an element in the linked list. Getting the kth smallest would cost only O(n) time
"""

class Solution(object):

    """
    - dfs: in-order traversal recursive
    - O(n), O(n) when tree is skewed (number of stacks needed)
    """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.kth_smallest = 0 # global variable
        def dfs(node, k):
            if k <= 0: # stop in-order traversal when kth_smallest is already found
                return 0
            if not node:
                return k
            k_remaining = dfs(node.left, k) # traverse left node
            if k_remaining == 1:
                self.kth_smallest = node.val
            k_remaining -= 1 # traverse itself
            k_remaining = dfs(node.right, k_remaining) # traverse right node
            return k_remaining
        
        dfs(root, k)
        return self.kth_smallest

    """
    - dfs: in-order traversal iterative
    - O(max(logN, k)), O(n) when tree is skewed (number of stacks needed)
    """
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4, None, None))
root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
s = Solution()
# s.kthSmallest(root, 1)
s.kthSmallest(root2, 3)
