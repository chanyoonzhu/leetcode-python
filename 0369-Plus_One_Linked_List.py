# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- LinkedList (recursive)
- O(n), O(n)
"""
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        head, carry = self.helper(head)
        if carry:
            return ListNode(1, head)
        return head 
            
        
    def helper(self, node):
        if not node:
            return (None, 1) # next, carry
        next, carry = self.helper(node.next)
        node.next = next
        node.val += carry
        if node.val == 10:
            node.val = 0
            return (node, 1)
        else:
            return (node, 0)

"""
- LinkedList (iterative)
- intuition: find last node with value != 9, add 1 to it, then turn all following into 0 (remember to add a dummy value at front)
- O(n), O(1)
"""
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        node = dummy
        while node:
            if node.val != 9:
                last_not_nine = node
            node = node.next
            
        last_not_nine.val += 1
        nine = last_not_nine.next
        while nine:
            nine.val = 0
            nine = nine.next
        
        return dummy if dummy.val else dummy.next