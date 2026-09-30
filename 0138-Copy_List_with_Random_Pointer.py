# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        """
        - O(n), O(n)
        - recursive with hashmap to store node address to avoid creating same node twice
        
        dic = {}
        return self.helper(head, dic)
        
    def helper(self, head, dic):
        
        if head is None:
            return None
        
        if head in dic:
            return dic[head]
        
        node = RandomListNode(head.label)
        
        dic[head] = node
        
        node.next = self.helper(head.next, dic)
        node.random = self.helper(head.random, dic)
        
        return node
        """
        
        """
        - O(n), O(n)
        - iterative with hashmap to store node address to avoid creating same node twice
        
        dic = {}
        
        if head is None:
            return None
        
        oldNode = head
        newNode = RandomListNode(oldNode.label)
        dic[oldNode] = newNode
        
        while oldNode:
            if oldNode.next:
                if oldNode.next in dic:
                    newNode.next = dic[oldNode.next]
                else:
                    newNode.next = RandomListNode(oldNode.next.label)
                    dic[oldNode.next] = newNode.next
            else:
                newNode.next = None
            if oldNode.random:
                if oldNode.random in dic:
                    newNode.random = dic[oldNode.random]
                else:
                    newNode.random = RandomListNode(oldNode.random.label)
                    dic[oldNode.random] = newNode.random
            else:
                newNode.random = None
                
            oldNode, newNode = oldNode.next, newNode.next
        
        return dic[head]
        """

        """
        - iterative method reuse

        def copyRandomList(self, head: 'Node') -> 'Node':
            if head is None: # head not in dict under this situation
                return None
            
            dict = {}
            new_node = self.copy_node(head, dict)
            pointer = head
            while pointer:
                new_node.next = self.copy_node(pointer.next, dict)
                new_node.random = self.copy_node(pointer.random, dict)
                pointer, new_node = pointer.next, new_node.next
            return dict[head]
        
        def copy_node(self, node: 'Node', dict: 'dict') -> 'Node':
            if node is None:
                return None
            if node in dict:
                return dict[node]
            else:
                node_copy = Node(node.val, None, None)
                dict[node] = node_copy
            return node_copy
        """
        
"""
- O(n), O(1)
- intuition: attach each copy node right next to its original node
- interleaving linkedlist
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # copy next pointers
        original = head
        while original:
            new = Node(original.val, original.next)
            original.next = new
            original = new.next
        
        # copy random pointers
        original = head
        while original:
            if original.random: # easy to miss
                original.next.random = original.random.next
            original = original.next.next
            
        # detach interleaved nodes
        original = head
        copy_head = head.next
        while original:
            copy = original.next
            original.next = copy.next
            if original.next: # easy to miss
                copy.next = original.next.next
            original = original.next
    
        return copy_head

"""
 
难点：一般的链表拷贝可以按顺序直接来，但是因为有random，random指向的是在遍历next的时候可能创建过的或者没有创建过的node，判断这个是一个难点。
1. 用hashmap建立新旧node的一一对应（旧->新），遍历的时候用hashmap检查，已经有的用reference，没有的就创建新的。
O(n), O(n)
2. 
上面解法的recursion版本
O(n), O(n)
3.
O(n), O(1)
"""