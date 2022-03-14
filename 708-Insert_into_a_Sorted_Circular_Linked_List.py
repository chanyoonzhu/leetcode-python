"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
"""
- two pointers
- O(n), O(1)
"""
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        def should_insert_in_between(prev, nextt):
            if not prev or not nextt:
                return False
            if prev.val <= insertVal <= nextt.val: # right in between
                return True
            if prev.val > nextt.val and (insertVal <= nextt.val or insertVal >= prev.val): # at circular point
                return True
            return False

        prev, nextt = None, head
        while not prev or nextt != head: # break when traversed the entire circle
            if should_insert_in_between(prev, nextt):
                prev.next = Node(insertVal, nextt)
                return head
            else:
                prev, nextt = nextt, nextt.next
        # need to be inserted as prev of head
        # tail -> prev
        prev.next = Node(insertVal, nextt)
        return head
        