# Clarification questions / assumptions:
# - Should each duplicated subtree shape be returned once, even if it appears
#   more than twice? Yes; return one representative node per duplicated shape.
# - Does the order of returned representatives matter? No; this DFS appends a
#   representative when it encounters the second copy in postorder.
# - Are node values integers? Yes, as in the problem; `|` is therefore safe as
#   a serialization delimiter.
# - Can the tree be empty? Yes; return an empty list.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """Find duplicate subtrees by serializing each subtree, updated October 2026.

    A postorder DFS builds a serialization from the node value and its left and
    right subtree serializations. Keep one set of all serializations and a
    second set to ensure each duplicate type contributes only one node.

    Time: O(n^2) worst case because constructing and storing all subtree
    strings can take quadratic total space and work for a skewed tree.
    Auxiliary space: O(n^2) for stored subtree strings in the worst case, plus
    O(h) recursion stack space, where h is the tree height.
    """

    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode]:
        serialized_all: set[str] = set()
        serialized_duplicated: set[str] = set()
        results: list[TreeNode] = []

        self._dfs(root, serialized_all, serialized_duplicated, results)
        return results

    def _dfs(
        self,
        root: TreeNode | None,
        serialized_all: set[str],
        serialized_duplicated: set[str],
        results: list[TreeNode],
    ) -> str:
        if not root:
            return ""

        left_serialized = self._dfs(
            root.left, serialized_all, serialized_duplicated, results
        )
        right_serialized = self._dfs(
            root.right, serialized_all, serialized_duplicated, results
        )
        tree_serialized = f"{root.val}|{left_serialized}|{right_serialized}"

        if tree_serialized in serialized_all:
            if tree_serialized not in serialized_duplicated:
                serialized_duplicated.add(tree_serialized)
                results.append(root)
        else:
            serialized_all.add(tree_serialized)

        return tree_serialized


# Interview-relevant test cases:
# Core behavior:
# - [1, 2, 3, 4, null, 2, 4, null, null, 4] -> representatives for [2, 4]
#   and [4], each returned once.
# - [1, 2, 3] -> [] (no duplicate subtrees).
# Boundaries and corner cases:
# - [] -> []
# - [1] -> []
# - [0, 0, 0] -> one representative for the leaf subtree [0].
