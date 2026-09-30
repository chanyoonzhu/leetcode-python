# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- LinkedList
- O(n), O(1)
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                dup = node.next
                node.next = dup.next
                del dup
            else: # easy to miss: do not move pointer if a node has been deleted to handle corner case (consecutive duplicates): [1, 1, 1]
                node = node.next
        return head