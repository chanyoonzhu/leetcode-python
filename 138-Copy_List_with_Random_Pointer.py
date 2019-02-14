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
        - O(n), O(1)
        - interleaving linkedlist
        """
        if head is None:
            return None
        
        oldNode = head
        
        # create interleaving list
        while oldNode:
            copy = RandomListNode(oldNode.label)
            copy.next = oldNode.next if oldNode.next else None
            oldNode.next = copy
            oldNode = oldNode.next.next
            
        # copy random pointer
        oldNode = head
        while oldNode:
            oldNode.next.random = oldNode.random.next if oldNode.random else None
            oldNode = oldNode.next.next
        
        # detach link
        oldNode = head
        copyHead = oldNode.next
        while oldNode:
            copy = oldNode.next
            if copy.next:
                oldNode.next = copy.next
                copy.next = copy.next.next
            else:
                oldNode.next = None
                copy.next = None
            oldNode = oldNode.next
        
        return copyHead