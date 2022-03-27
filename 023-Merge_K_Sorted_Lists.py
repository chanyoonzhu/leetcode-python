# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
- priority queue - python2 solution
- O(nlogk) k: number of, O(n)
- intuition
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
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

"""
- same solution Python3 
(at any time in the priority queue, the i will be unique. Use the unique i as a tie breaker so that it doesn't compare two listnodes, which will throw an error)
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = [(list_.val, i, list_) for i, list_ in enumerate(lists) if list_]
        heapq.heapify(q)
        ptr = head = ListNode()
        
        while q:
            val, i, node = heapq.heappop(q)
            ptr.next = node
            ptr = ptr.next
            if node.next:
                heapq.heappush(q, (node.next.val, i, node.next))
                
        return head.next

"""
- same as previous, move linkedlist pointer after traversal
- O(Nlogk), O(n)
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ptr = ListNode()
        h = [] # number, list index
        for i, l in enumerate(lists):
            if l:
                h.append((l.val, i))
                lists[i] = l.next
        heapq.heapify(h)
        while h:
            x, i = heapq.heappop(h)
            ptr.next = ListNode(x)
            ptr = ptr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        return res.next

"""
- same as previous, modify in-place
- O(Nlogk), O(n)
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ptr = ListNode()
        h = [] # number, list index
        for i, l in enumerate(lists):
            if l:
                h.append((l.val, i))
        heapq.heapify(h)
        while h:
            x, i = heapq.heappop(h)
            ptr.next = lists[i]
            ptr = ptr.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(h, (lists[i].val, i))  
        return res.next
            