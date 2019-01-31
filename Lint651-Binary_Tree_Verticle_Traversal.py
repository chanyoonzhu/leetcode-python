
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """

    """
    - O(nlog(n))
    - O(n)
    - index the verticle level as we do BFS of the tree
    - store index in hashmap and then sort
    """
    def verticalOrder(self, root):
        # write your code here
        if root is None:
            return []
            
        dic = {}
        q = [(root, 0)]
        while q:
            curr = q[0]
            del q[0]
            if curr[1] not in dic:
                dic[curr[1]] = [curr[0].val]
            else:
                dic[curr[1]].append(curr[0].val)
            if curr[0].left is not None:
                q.append((curr[0].left, curr[1] - 1))
            if curr[0].right is not None:
                q.append((curr[0].right, curr[1] + 1))
        
        res = [t[1] for t in sorted(dic.items(), key=lambda x:x[0])]
        
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sl = Solution()
print(sl.verticalOrder(root))

