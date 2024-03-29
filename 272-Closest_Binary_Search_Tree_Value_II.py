# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- bst search + heap
- O(logn*logk)?
"""
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        
        def binary_search(node):
            if not node:
                return
            
            heapq.heappush(heap, (-abs(node.val - target), node.val))
            is_node_in_k = True
            if len(heap) > k:
                _, val_out = heapq.heappop(heap)
                if val_out == node.val: # node got popped, node is not a candidate
                    is_node_in_k = False
                    if node.val > target:
                        # only traverse left side, right will be even farther than node is to the target
                        binary_search(node.left)
                    else:
                        # don't traverse left, left will be even farther
                        binary_search(node.right)
            if is_node_in_k: # need traverse both sides
                if node.val > target:
                    binary_search(node.left) # left side has better chance of being closer
                    binary_search(node.right)
                else:
                    binary_search(node.right) # right side has better chance of being closer
                    binary_search(node.left)
            
        binary_search(root)
        return [val for _, val in heap]

"""
- dfs (inorder-traversal)
- O(logn)?
"""
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        queue = deque() # inorder traversal guarantees values in queue is increasing
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            
            if len(queue) < k:
                queue.append(node.val)
                dfs(node.right)
            else:
                if abs(queue[0] - target) > abs(node.val - target):
                    queue.append(node.val)
                    queue.popleft()
                    dfs(node.right)
                else:
                    return
        
        dfs(root)
        return queue