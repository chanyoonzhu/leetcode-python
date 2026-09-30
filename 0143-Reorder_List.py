# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- Linkedlist with slow and fast pointers
- O(n), O(1)
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # find middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half 
        prev, cur = None, slow.next
        while cur:
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        slow.next = None # caveat: don't forget to reset tail
        
        # merge two linkedlist
        head1, head2 = head, prev
        while head2:
            next1, next2 = head1.next, head2.next
            head1.next = head2
            head2.next = next1
            head1, head2 = next1, next2
        return head
            
        
            
        