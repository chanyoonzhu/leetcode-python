# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    - hashmap: find parent trace for all target nodes, then find lca
    - O(kn), O(kn)
    - TimeLimitExceeded
    """
    def lowestCommonAncestor(self, root, nodes):
        parent_map = dict()
        parent_map[root] = None
        
        parents_lists = [[] for _ in nodes]
        
        def populate_parent_map(node):
            if not node:
                return
            if node.left:
                parent_map[node.left] = node
                populate_parent_map(node.left)
            if node.right:
                parent_map[node.right] = node
                populate_parent_map(node.right)
        
        populate_parent_map(root)
        for i, node in enumerate(nodes):
            while node:
                parents_lists[i].insert(0, node)
                node = parent_map[node]
        
        lowest_height = min(len(parents) for parents in parents_lists)
        for i in range(lowest_height - 1, -1, -1):
            if all(parents[i] == parents_lists[0][i] for parents in parents_lists):
                return parents_lists[0][i]
    
    """
    - dfs recursive: find lca pair by pair
    """
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        def lowestCommonAncestorForTwoNodes(node, p, q):
            if not node or node == p or node == q:
                return node
            
            left = lowestCommonAncestorForTwoNodes(node.left, p, q)
            right = lowestCommonAncestorForTwoNodes(node.right, p, q)
            
            if left and right:
                return node
            
            return left if left else right
        
        lca = nodes[0]
        for i in range(1, len(nodes)):
            lca = lowestCommonAncestorForTwoNodes(root, lca, nodes[i])
        return lca
    
    """
    - dfs recursive
    """
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        nodes_pool = set(nodes)
        
        def dfs(node):
            if not node or node in nodes_pool:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            
            return left or right
        
        return dfs(root)


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
print(sl.lowestCommonAncestor(n1, [n8, n9]).val)