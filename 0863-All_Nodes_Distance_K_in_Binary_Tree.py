# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- dfs - two dfs, one for traverse child, one for provide info for parent
- O(n), O(n)
"""
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.result = []
        
        def dfs(node): # returns distance to its decendant target + 1
            if not node:
                return -1
            if node is target:
                subtree_add(node, K)
                return 1
            l_distance_to_target, r_distance_to_target = dfs(node.left), dfs(node.right)
            if l_distance_to_target == K or r_distance_to_target == K:
                self.result.append(node.val)
                return K + 1
            if 0 < l_distance_to_target <= K:
                l_distance_to_target += 1
                subtree_add(node.right, K - l_distance_to_target)
                return l_distance_to_target
            if 0 < r_distance_to_target < K:
                r_distance_to_target += 1
                subtree_add(node.left, K - r_distance_to_target)
                return r_distance_to_target
            return -1
            
        def subtree_add(node, distance):
            if not node:
                return
            if distance == 0:
                self.result.append(node.val)
                return
            subtree_add(node.left, distance - 1)
            subtree_add(node.right, distance - 1)
            
        dfs(root)
        return self.result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- dfs - two dfs, one for traverse child, one for provide info for parent
- O(n), O(n)
"""
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        root_to_target = [] # 0 - left, 1 - right
        res = []
        
        def findParentPath(node, path):
            if not node:
                return None
            if node.val == target.val:
                return path
            l = findParentPath(node.left, path + [0])
            r = findParentPath(node.right, path + [1])
            return l or r
            
        def dfs(node, k):
            if not node:
                return
            if k == 0:
                res.append(node.val)
            dfs(node.left, k-1)
            dfs(node.right, k-1)
            
        root_to_target = findParentPath(root, [])
        dfs(target, k) # find decendents with distance k
        # find nodes with distance k that are not decendents
        parent_node = root
        for i, direction in enumerate(root_to_target):
            dist = len(root_to_target) - i # dist to target
            if dist < k:
                if direction == 0:
                    dfs(parent_node.right, k - dist - 1)
                else:
                    dfs(parent_node.left, k - dist - 1)
            elif dist == k:
                res.append(parent_node.val)
            parent_node = parent_node.left if direction == 0 else parent_node.right
        return res

"""
- graph + bfs : todo
- O(n), O(n)
"""
        