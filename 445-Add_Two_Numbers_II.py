# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """
        s1, s2 = [], []
        ptr1, ptr2 = l1, l2
        carry = sum_ = 0
        sSum = []
        
        while ptr1:
            s1.append(ptr1.val)
            ptr1 = ptr1.next
            
        while ptr2:
            s2.append(ptr2.val)
            ptr2 = ptr2.next
            
        while s1 or s2 or carry:
            if not s1 and not s2:
                ptrSum.next = ListNode(carry)
                carry = 0
            else:
                val1 = val2 = 0
                if not s1:
                    sum_ = s2.pop() + carry
                elif not s2:
                    sum_ = s1.pop() + carry
                
                carry, sum_ = divmod(sum_, 10)
                
                sSum.append = sum
                
                ptrSum = ptrSum.next
                
        return lSum.next
        numList = ListNode(0)
        """
        
        
        n1 = self.listToNumber(l1, 0)
        n2 = self.listToNumber(l2, 0)
        _sum = n1 + n2
        sumStr = str(_sum)
        self.numberToList(sumStr, numList)
        return numList.next
        
    def listToNumber(self, l: ListNode, n: int) -> int:
        if l is None:
            return n
        n = n * 10 + l.val
        return self.listToNumber(l.next, n)
    
    def numberToList(self, n: str, l: ListNode) -> ListNode:
        if n == '':
            return l
        digit = ord(n[0]) - ord('0')
        l.next = ListNode(digit)
        return self.numberToList(n[1:], l.next)

l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(Solution().addTwoNumbers(l1, l2))