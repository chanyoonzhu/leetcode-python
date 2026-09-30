# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- merge sort
- O(nlogn)
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = self.split(head)
        if head1 == head2:
            return head1
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.merge(head1, head2)
    
    def split(self, head):
        slow = fast = head
        slow_prev = None
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        if slow_prev: slow_prev.next = None
        return (head, slow)
    
    def merge(self, head1, head2):
        ptr1, ptr2 = head1, head2
        ptr = head = TreeNode()
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            ptr = ptr.next
        if ptr1:
            ptr.next = ptr1
        if ptr2:
            ptr.next = ptr2
        return head.next

"""
- merge sort buttom up
- O(nlogn), O(1)
"""