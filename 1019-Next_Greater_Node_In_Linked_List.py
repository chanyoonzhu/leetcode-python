# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
- monotonically decreasing stack
- O(n), O(n)
"""
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        result = []
        while head:
            val = head.val
            while stack and val > stack[-1][0]:
                result[stack.pop()[1]] = val
            stack.append((val, len(result)))
            result.append(0)
            head = head.next
        return result