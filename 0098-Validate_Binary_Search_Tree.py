# Clarification questions / assumptions:
# - Are duplicate values allowed? LeetCode 98 requires every value to be strictly
#   between its ancestor bounds, so duplicates are invalid.
# - What values can nodes contain? LeetCode 98 uses integers; the bounds-based
#   implementation also uses +/- infinity as sentinels.
# - Can a node value be null? No; null represents a missing child, not a node
#   value.
# - Is an empty tree valid? Yes; it is a valid BST.

# Definition for a binary tree node:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class IncorrectLocalChecksSolution:
    """Known incorrect approach, documented September 2026.

    This checks each node only against its immediate children. A BST also
    requires every node to obey the bounds imposed by all its ancestors. For
    example, in [5, 1, 7, null, null, 4, 8], node 4 is a descendant in the
    right subtree of 5, so it must be greater than 5. The local checks pass:
    4 is less than its parent 7, and each immediate parent-child pair is
    ordered, but the tree is not a BST because 4 is less than ancestor 5.

    Time: O(n) in the worst case.
    Auxiliary space: O(h) for recursive calls, where h is tree height.
    """

    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)


class Solution:
    """Correct bounds-based approach, documented September 2026.

    Each recursive call carries the valid value range from its ancestors, so
    values deeper in a subtree are checked against every relevant ancestor.
    The explicit child comparisons and min/max bounds are correct but
    redundant; a cleaner version checks the current node against low/high
    directly, then passes root.val as the updated bound.

    Time: O(n).
    Auxiliary space: O(h) for recursive calls, where h is tree height.
    """

    def isValidBST(self, root: TreeNode | None) -> bool:
        return self._dfs(root, float("-inf"), float("inf"))

    def _dfs(self, root: TreeNode | None, low: float, high: float) -> bool:
        if not root:
            return True
        if root.left and (root.left.val >= root.val or root.left.val <= low):
            return False
        if root.right and (root.right.val <= root.val or root.right.val >= high):
            return False
        return self._dfs(root.left, low, min(root.val, high)) and self._dfs(
            root.right, max(root.val, low), high
        )


class Solution:
    """Optimal bounds-based validation, documented September 2026.

    Carry the strict lower and upper bounds imposed by all ancestors. Reject
    the current value when it is outside that range, then tighten the range
    for each subtree. This checks each node once and avoids child-specific
    checks and redundant min/max operations.

    Time: O(n), where n is the number of nodes.
    Auxiliary space: O(h) for recursive calls, where h is tree height.
    """

    def isValidBST(self, root: TreeNode | None) -> bool:
        return self._dfs(root, float("-inf"), float("inf"))

    def _dfs(self, root: TreeNode | None, low: float, high: float) -> bool:
        if not root:
            return True
        if root.val >= high or root.val <= low:
            return False
        return self._dfs(root.left, low, root.val) and self._dfs(
            root.right, root.val, high
        )


# Interview-relevant test cases for validating a correct BST solution:
# Core behavior:
# - [2, 1, 3] -> True
# - [5, 1, 7, null, null, 4, 8] -> False (ancestor-bound violation missed by
#   IncorrectLocalChecksSolution)
# Boundaries and corner cases:
# - [] -> True
# - [1] -> True
# - [2, 2, 3] -> False (duplicate violates strict ordering)
