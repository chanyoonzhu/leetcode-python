# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        """
        - O(max(m, n)), O(max(m, n))
        - recursive
        
        return self.helper(l1, l2, 0)
        
    def helper(self, l1, l2, carry):
        if not l1 and not l2:
            if not carry:
                return None
            else:
                return ListNode(carry)
        
        sum_ = carry
        if l1: sum_ += l1.val
        if l2: sum_ += l2.val
        
        carry, sum_ = divmod(sum_, 10)
        node = ListNode(sum_)
        if not l1:
            node.next = self.helper(l1, l2.next, carry)
        elif not l2:
            node.next = self.helper(l1.next, l2, carry)
        else:
            node.next = self.helper(l1.next, l2.next, carry)
            
        return node
        """
        
        """
        - Iterative
        """
        
        head = ptr = ListNode(0)
        carry = sum_ = 0
        
        while l1 or l2 or carry:
            
            val1 = val2 = 0
            if l1: 
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            
            sum_ = val1 + val2 + carry
            carry, sum_ = divmod(sum_, 10)
            
            ptr.next = ListNode(sum_)
            ptr = ptr.next
        
        return head.next