# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    - dfs recursive: returns true when one descendent equals p or q, false otherwise. When has true on both left and right path, mark as common ancestor
    - Time: (O(n)), Space: O(n)
    """
     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(node, p, q):
            if node is None:
                return False
            curr = node == p or node == q
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left + right + curr == 2:
                self.ans = node

            return left or right or curr
        
        dfs(root, p, q)
        return self.ans
    
    """
    - hashmap + hashset
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
        
        if p not in parent_map or q not in parent_map:
            return None
        
        while p:
            ancestors.add(p)
            p = parent_map[p]
        
        while q not in ancestors:
            q = parent_map[q]
            return q

n1 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(1)
n4 = TreeNode(6)
n5 = TreeNode(2)
n6 = TreeNode(0)
n7 = TreeNode(8)
n8 = TreeNode(7)
n9 = TreeNode(4)

n10 = TreeNode(10)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9

sl = Solution()
print(sl.lowestCommonAncestor(n1, n2, n9).val)
        