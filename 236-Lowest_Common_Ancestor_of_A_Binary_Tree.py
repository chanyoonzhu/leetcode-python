import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    self.ans = None

    def lowestCommonAncestor(self, root, p, q):

        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        """
        - O(n), O(n)
        """

    self.traverseTree(root)
    return self.ans

    def traverseTree(self, root):

        left = self.traverseTree(root.left)
        right = self.traverseTree(root.right)

        mid = root == p or root == q
        
        if mid + left + right >= 2:
            self.ans = root
        
        return mid or left or right

        """
        - O(n), O(n)

        parents = {}
        self.traverseTree(root, parents)
        
        qParents = self.findAllParents(q, parents)
        pParentsSet = set(self.findAllParents(p, parents))
        for i in range(len(qParents)): # df: qParents is in reverse order already
            if qParents[i] in pParentsSet:
                return qParents[i]
     
    def traverseTree(self, root, parents):
        if root is None:
            return
        if root.left:
            parents[root.left] = root # to append all parents of its parent, not just its direct parent
            self.traverseTree(root.left, parents)
        if root.right:
            parents[root.right] = root
            self.traverseTree(root.right, parents)

    def findAllParents(self, node, parents):
        res = [node] # don't forget: itself is also it's parent
        curr = node
        while curr in parents:
            res.append(parents[curr])
            curr = parents[curr]
        return res
        """

        """
        - O(n)
        - memory exceeded

        parents = collections.defaultdict(list)
        self.traverseTree(root, parents)
       
        qParents = parents[q]
        pParentsSet = set(parents[p])
        for i in range(len(qParents)-1, -1, -1):
            if qParents[i] in pParentsSet:
                return qParents[i]
     
    def traverseTree(self, root, parents):
        if root is None:
            return
        parents[root].append(root) # don't forget to append itself as parent
        if root.left:
            parents[root.left] += parents[root] # to append all parents of its parent, not just its direct parent (memory problem)
            self.traverseTree(root.left, parents)
        if root.right:
            parents[root.right] += parents[root]
            self.traverseTree(root.right, parents)
        """
        

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
print(sl.lowestCommonAncestor(n1, n2, n9))

