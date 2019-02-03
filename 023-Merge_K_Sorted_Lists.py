# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """
        - O(nlog(k))
        priority queue
        put the 1st element of each row into a queue, pop and push the one following it until all popped out
        """
        import heapq
        heap = []
        res = pointer = ListNode(0)
        
        for head in lists:
            if head is not None:
                heapq.heappush(heap, (head.val, head))
            
        while len(heap):
            pointer.next = heapq.heappop(heap)[1]
            if pointer.next.next is not None:
                heapq.heappush(heap, (pointer.next.next.val, pointer.next.next))
            pointer = pointer.next
        
        return res.next
            