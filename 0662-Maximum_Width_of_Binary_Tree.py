# Clarification questions / assumptions:
# - Does width include missing nodes between the leftmost and rightmost nodes
#   on a level? Yes; count their positions in the complete-tree layout.
# - Can the tree be empty? Yes; its width is 0.

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """Track each level's extreme positions with recursive DFS, updated
    October 2026.

    Time: O(n), visiting each node once.
    Auxiliary space: O(h) for recursion and O(h) stored level boundaries.
    """

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Each entry stores the leftmost and rightmost position seen at a depth.
        left_right = []
        self.dfs(root, 0, 0, left_right)
        res = 0
        for left, right in left_right:
            # Positions include gaps, so the width is the inclusive span.
            res = max(res, right - left + 1)
        return res

    def dfs(self, node, row, col, left_right):
        if not node:
            return

        # Visit left-to-right: the first node seen at a row sets both bounds.
        if row == len(left_right):
            left_right.append((col, col))
        else:
            # Later nodes may extend that row's right boundary.
            left, right = left_right[row]
            left_right[row] = (min(left, col), max(right, col))

        # Complete-tree positions preserve missing-node gaps: left=2*col,
        # right=2*col+1. For example, root position 0 has children at 0 and 1.
        self.dfs(node.left, row + 1, col * 2, left_right)
        self.dfs(node.right, row + 1, col * 2 + 1, left_right)

"""
- bfs
"""


class Solution:
    """Calculate widths with absolute BFS positions, added October 2026.

    Visit only real nodes and assign each its position in the complete-tree
    layout. The minimum and maximum positions on each level give that level's
    width, including any gaps between nodes.

    Time: O(n) queue operations.
    Auxiliary space: O(w), where w is the maximum number of real nodes on a
    level.

    Limitation: indices are not normalized, so they can grow to O(h) bits on
    a deep, sparse tree. Python integers do not overflow, but arithmetic and
    storage become more expensive as those indices grow. The following
    normalized BFS keeps the position values smaller.
    """

    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue_cur = deque([(root, 0)])
        max_width = 0

        while queue_cur:
            queue_next: deque[tuple[TreeNode, int]] = deque()
            left_idx = float("inf")
            right_idx = float("-inf")

            for node, node_idx in queue_cur:
                left_idx = min(left_idx, node_idx)
                right_idx = max(right_idx, node_idx)

                if node.left:
                    queue_next.append((node.left, node_idx * 2))
                if node.right:
                    queue_next.append((node.right, node_idx * 2 + 1))

            max_width = max(max_width, right_idx - left_idx + 1)
            queue_cur = queue_next

        return max_width


class Solution:
    """Single-queue BFS with absolute positions, added October 2026.

    The queue contains one level followed by its children as they are
    discovered. Capture the current queue length before processing so newly
    appended children wait until the next iteration. The first and last
    positions give the level width, including missing positions in between.

    Time: O(n) queue operations.
    Auxiliary space: O(w), where w is the maximum number of real nodes on a
    level.

    Limitation: positions are not normalized, so integer indices can grow to
    O(h) bits on a deep, sparse tree. The normalized BFS below reduces this
    growth.
    """

    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 1

        while queue:
            level_size = len(queue)
            width = queue[-1][1] - queue[0][1] + 1
            max_width = max(max_width, width)

            for _ in range(level_size):
                node, node_idx = queue.popleft()
                if node.left:
                    queue.append((node.left, node_idx * 2))
                if node.right:
                    queue.append((node.right, node_idx * 2 + 1))

        return max_width


class Solution:
    """Cleaner normalized BFS solution, added October 2026.

    Keep only real nodes in the queue and assign each its complete-tree
    position. The difference between the first and last positions captures
    gaps from missing nodes. Normalize positions against the first position
    on every level so very deep trees do not accumulate unnecessarily large
    absolute indices.

    Time: O(n), where n is the number of nodes.
    Auxiliary space: O(n) in the worst case for the BFS queue.

    Limitation: position values can still need O(h) bits for a level with a
    large positional gap, where h is the tree height; normalization prevents
    their magnitude from growing across levels without changing the width.
    """

    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            first_position = queue[0][1]
            last_position = queue[-1][1]
            max_width = max(max_width, last_position - first_position + 1)

            for _ in range(len(queue)):
                node, position = queue.popleft()
                position -= first_position

                if node.left:
                    queue.append((node.left, 2 * position))
                if node.right:
                    queue.append((node.right, 2 * position + 1))

        return max_width


class TLEPlaceholderExpansion:
    """Documented TLE approach, added October 2026.

    This version retains missing positions as None and expands each None into
    two more None placeholders on the next level. A sparse tree of height h
    can therefore create O(2^h) queue entries despite having only O(h) real
    nodes. The placeholder queue causes the time and memory limit to be
    exceeded; queue only real nodes and track their positional indices instead.

    Time: O(2^h) in the worst case before the all-empty level is reached.
    Auxiliary space: O(2^h) for the expanded placeholder queue.
    """

    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue_cur = deque([root])
        max_width = 1

        while True:
            left_idx = -1
            right_idx = len(queue_cur)
            queue_next = deque()

            for index, node in enumerate(queue_cur):
                if index == left_idx + 1 and node is None:
                    left_idx = index

                if node:
                    queue_next.append(node.left)
                    queue_next.append(node.right)
                else:
                    queue_next.append(None)
                    queue_next.append(None)

            for offset, node in enumerate(reversed(queue_cur)):
                position = len(queue_cur) - offset - 1
                if position == right_idx - 1 and node is None:
                    right_idx = position

            width = right_idx - left_idx - 1
            max_width = max(max_width, width)
            queue_cur = queue_next

            if width < 0:
                return max_width


# Interview-relevant test cases:
# Core behavior:
# - [1, 3, 2, 5, 3, null, 9] -> 4
# - [1, 1, 1, 1, 1, 1, 1, null, null, null, 1, null, null, null, null,
#    2, 2, 2, 2, 2, 2, 2, null, 2, null, null, 2, null, 2] -> 8
# Boundaries and corner cases:
# - [] -> 0
# - [1] -> 1
