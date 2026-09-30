# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
- reverse a linkedlist (recursive)
- O(n), O(n/k)
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        count = 0
        ptr = head
        
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        if count < k:
            return head
        
        new_next, cur = None, head
        for _ in range(k):
            old_next = cur.next
            cur.next = new_next
            new_next, cur = cur, old_next

        head.next = self.reverseKGroup(cur, k)
        return new_next

"""
- reverse a linkedlist (iterative)
- O(n), O(n/k)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        groups = count = 0
        dummy_head = ListNode()
        dummy_head.next = head
        ptr = head
        
        # get number of groups
        while ptr:
            ptr = ptr.next
            count += 1
            if count == k:
                groups += 1
                count = 0
    
        group_prev_end = dummy_head
        while groups:
            group_start = group_prev_end.next
            
            prev, cur = None, group_start
            for _ in range(k):
                nextt = cur.next
                cur.next = prev
                prev, cur = cur, nextt 
            
            group_prev_end.next = prev # new start
            group_prev_end = group_start # new end
            group_start.next = nextt
            groups -= 1
        
        return dummy_head.next
            
            
            