# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- two pointers
- O(max(k, n)), O(1)
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        N = 0
        ptr1 = ptr2 = head # ptr1 - slower, ptr2 - faster by k
        
        while k and ptr2: 
            ptr2 = ptr2.next
            k -= 1
            N += 1
        if k: # when k > len(linkedlist)
            k %= N 
            ptr2 = head
            while k:
                ptr2 = ptr2.next
                k -= 1
        if not ptr2: ptr2 = head # easy to miss
            
        
        if ptr1 == ptr2:
            return head
        
        while ptr2.next: # move ptr1 to one node before new head
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        new_head = ptr1.next
        ptr1.next = None
        ptr2.next = head
        return new_head
        
        
        
        
            
        
        