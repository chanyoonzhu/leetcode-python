# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':

        
        beforeList = beforePtr = ListNode(0)
        afterList = afterPtr = ListNode(0)
        
        while head is not None:
            if head.val < x:
                beforePtr.next = head
                beforePtr = beforePtr.next
            else:
                afterPtr.next = head
                afterPtr = afterPtr.next
            head = head.next
            
        afterPtr.next = None
        
        beforePtr.next = afterList.next
        return beforeList.next

head = ListNode(2)
head.next = ListNode(1)

# head = ListNode(1)
# head.next = ListNode(4)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(2)
print(Solution().partition(head, 2))