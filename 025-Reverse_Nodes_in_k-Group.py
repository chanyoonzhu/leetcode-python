class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):

        """
        if k == 0 or k == 1: return head
        dummy = ListNode(0)
        dummy.next = head
        nextDummy = dummy
        while nextDummy.next:
            count = 0
            thisDummy = nextDummy
            while nextDummy.next and count < k:
                nextDummy = nextDummy.next
                count += 1
            if count == k:
                end = thisDummy.next
                for _ in range(count-1):
                    thisHead = end.next
                    end.next = thisHead.next
                    thisHead.next = thisDummy.next
                    thisDummy.next = thisHead
                nextDummy = end
            else:
                break
        return dummy.next
        """
        
        """
        recursive?
        """

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s.reverseKGroup(head, 2)
            
            