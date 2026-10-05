# Clarification questions / assumptions:
# - Should the traversal start left-to-right? Yes, the first level is
#   left-to-right and directions alternate at each level.
# - Can the tree be empty? Yes; return an empty list.

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """Breadth-first zigzag traversal, updated October 2026.

    Process one level at a time with two queues. Append each value to a deque
    on the right for left-to-right levels and on the left for right-to-left
    levels, avoiding the repeated shifts caused by list.insert(0, value).

    Time: O(n), where n is the number of nodes.
    Auxiliary space: O(n) for the queues and output values.
    """

    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        output: list[list[int]] = [[]]
        queue1 = deque([root])  # Nodes in the level being traversed.
        queue2 = deque()  # Nodes in the next level.
        left_to_right = True

        while True:
            level_values = deque()
            for node in queue1:
                if left_to_right:
                    level_values.append(node.val)
                else:
                    level_values.appendleft(node.val)

                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)

            output[-1] = list(level_values)
            queue1, queue2 = queue2, deque()
            if not queue1:
                return output

            left_to_right = not left_to_right
            output.append([])  # Add a row only when another level exists.


# Interview-relevant test cases:
# Core behavior:
# - [3, 9, 20, null, null, 15, 7] -> [[3], [20, 9], [15, 7]]
# - [1, 2, 3, 4, 5] -> [[1], [3, 2], [4, 5]]
# Boundaries and corner cases:
# - [] -> []
# - [1] -> [[1]]
