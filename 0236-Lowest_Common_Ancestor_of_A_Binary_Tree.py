import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    """
    - hashmap + set: keep a map of child to parent, and a set for all parents of p, search if parents for q from bottom to top is in the set
    - O(n), O(n)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_map = dict()
        parent_map[root] = None
        ancestors = set()
        
        def create_parents(node):
            if node:
                if node.left:
                    parent_map[node.left] = node
                    create_parents(node.left)
                if node.right:
                    parent_map[node.right] = node
                    create_parents(node.right)
        
        create_parents(root)
        
        while p:
            ancestors.add(p)
            p = parent_map[p]

        while q not in ancestors:
            q = parent_map[q]
        return q
    
    """
    - dfs recursive: returns true when one descendent equals p or q, false otherwise. When has true on both left and right path, mark as common ancestor
    - Time: (O(n)), Space: O(n)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans = None
        self.helper(root, p, q)
        return self.ans
        
    def helper(self, root, p, q):
        
        if not root:
            return False
        
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        
        mid = root == p or root == q
        
        if mid + left + right == 2:
            self.ans = root
            
        return mid or left or right
    
    """
    - dfs recursive: variation, this approach won't work for problem#1644 when p is q's ancestor or the other way around since it returns as soon as it sees one matching node
    - Time: (O(n)), Space: O(n)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == None or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right
        

n1 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(1)
n4 = TreeNode(6)
n5 = TreeNode(2)
n6 = TreeNode(0)
n7 = TreeNode(8)
n8 = TreeNode(7)
n9 = TreeNode(4)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9

sl = Solution()
print(sl.lowestCommonAncestor_iterative(n1, n2, n9))

