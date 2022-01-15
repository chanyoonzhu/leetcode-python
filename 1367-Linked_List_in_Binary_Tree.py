# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- dfs
- TLE
"""
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        if not head:
            return True
        if not root:
            return False
        if head.val == root.val:
            if self.isSubPath(head.next, root.left) or self.isSubPath(head.next, root.right):
                return True
        if self.isSubPath(head, root.left) or self.isSubPath(head, root.right):
                return True
        return False

"""
- dfs
- O(nl), O(n)
"""
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        if not head:
            return True
        if not root:
            return False
        if root.val == head.val and self.isIdentical(head, root): # if root match, check if identical
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def isIdentical(self, head, root):
        if not head:
            return True
        if not root or head.val != root.val:
            return False
        return self.isIdentical(head.next, root.left) or self.isIdentical(head.next, root.right)

"""
- dfs
- O(n*l), O(n)
"""
class Solution:
    def isSubPath(self, head, root, is_consecutive = False):
        if not head: return True
        if not root: return False
        if is_consecutive:
            if head.val != root.val: return False
            return self.isSubPath(head.next, root.left, True) or self.isSubPath(head.next, root.right, True)
        return self.isSubPath(head, root, True) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

"""
- todo: prefix
- O(n + l)
"""
            
        