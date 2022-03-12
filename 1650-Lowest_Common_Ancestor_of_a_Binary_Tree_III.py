"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

"""
- hashset
- O(h), O(h), h = n in worst case
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        p_ancestor = set()
        
        while p:
            p_ancestor.add(p)
            p = p.parent
        
        while q not in p_ancestor:
            q = q.parent
        return q
    
"""
- two pointers: 
- instinct: for each node to travel to ancestor after 1 switch, p travels: p to a (ancestor), a to root, q to a; q travels: q to a, a to root, p to a => the distance they travel are equal
- O(h), O(1), h = n in worst case
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        p1, q1 = p, q
        while p1 != q1:
            p1 = p1.parent if p1.parent else q
            q1 = q1.parent if q1.parent else p
        return p1