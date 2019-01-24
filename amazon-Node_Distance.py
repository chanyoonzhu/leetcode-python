class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def nodeDistance(nums, x, y):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    def helper(nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        res = TreeNode(nums[mid])
        res.left = helper(nums, start, mid - 1)
        res.right = helper(nums, mid + 1, end)
        return res

    def lowestCommonAncestor(root, p, q):
        

        if p < root.val and q < root.val:
            return lowestCommonAncestor(root.left, p, q)
        elif p > root.val and q > root.val:
            return lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def findLevel(root, x):
        if not root:
            return 0
        if root.val == x:
            return 0
        elif root.val > x:
            return findLevel(root.left, x) + 1
        else:
            return findLevel(root.right, x) + 1
        
    if x not in nums or y not in nums:
        return -1

    nums = sorted(nums)

    bst = helper(nums, 0, len(nums) - 1)   
    lca = lowestCommonAncestor(bst, x, y)
    xLevel = findLevel(bst, x) 
    yLevel = findLevel(bst, y)
    lcaLevel = findLevel(bst, lca.val)
    return xLevel + yLevel - 2 * lcaLevel

nums = [-10,-3,0,5,9]
print(nodeDistance(nums, 5, 9))

    
        
    