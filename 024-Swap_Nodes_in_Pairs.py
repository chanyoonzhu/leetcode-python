# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        origin = ListNode(0)
        origin.next = head
        ptr = origin
        
        while ptr.next:
            if ptr.next.next is None:
                break
            else:
                oldHead = ptr.next
                newHead = ptr.next.next
                nextHead = newHead.next
                newHead.next = oldHead
                oldHead.next = nextHead
                ptr.next = newHead
                ptr = oldHead
                
        return origin.next