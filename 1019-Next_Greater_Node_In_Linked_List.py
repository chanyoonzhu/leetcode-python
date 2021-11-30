# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
- monotonically decreasing stack
- O(n), O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        res = []
        stack = []
        index = 0
        
        while head:
            res.append(0) # append a dummy value so L28 won't go out of bound
            val = head.val
            
            while stack and stack[-1][0] < val:
                prev_idx = stack.pop()[1]
                res[prev_idx] = val

            stack.append((val, index))
            index += 1
            head = head.next

        return res