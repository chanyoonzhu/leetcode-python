# Clarification questions / assumptions:
# - Is the linked list sorted in ascending order? Yes, as required by the
#   problem.
# - Are duplicate values allowed? The usual LeetCode constraints use unique
#   values; the tree construction also works with nondecreasing input.
# - Can the list be empty? Yes; return an empty tree.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- LinkedList and BST
- O(nlogn), O(logn) - for recursion (balanced, not skewed)
"""
class Solution:
    """Build a balanced BST by choosing each linked-list midpoint. This solution
    saves space at the cost of modifying the LinkedList.

    Time: O(n log n), since each recursive level scans its list segment.
    Auxiliary space: O(log n) for the balanced recursion stack.
    """

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # The slow pointer moves one step while fast moves two, so slow lands
        # at the middle when fast reaches the end. Choosing a middle node keeps
        # the left and right subtrees as close in size as possible.
        slow = fast = head
        slow_parent = head
        while fast and fast.next: # fast, not head
            slow_parent = slow
            slow = slow.next # not head.next
            fast = fast.next.next # not head.next.next

        # Cut before the middle so the left recursion cannot include the root
        # again; the right side starts at the middle node's original successor.
        slow_parent.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


class Solution:
    """Working array-and-slicing approach, documented October 2026.

    Copy the sorted list values into an array, choose the middle value as each
    subtree root, then recursively build the left and right subtrees from
    slices. It is simpler to follow than repeated linked-list midpoint scans,
    but slicing copies values at each level and makes the total time O(n log n).

    Time: O(n log n), due to copying slices across recursion levels.
    Auxiliary space: O(n), for the values array and recursive slice copies;
    recursion depth is O(log n) because the resulting tree is balanced.
    """

    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        values: list[int] = []
        while head:
            values.append(head.val)
            head = head.next
        return self._list_to_bst(values)

    def _list_to_bst(self, values: list[int]) -> TreeNode | None:
        if not values:
            return None

        middle = len(values) // 2
        root = TreeNode(values[middle])
        root.left = self._list_to_bst(values[:middle])
        root.right = self._list_to_bst(values[middle + 1 :])
        return root


# Interview-relevant test cases:
# Core behavior:
# - [-10, -3, 0, 5, 9] -> a height-balanced BST containing all values.
# - [1, 3] -> a height-balanced BST containing both values.
# Boundaries and corner cases:
# - [] -> None
# - [0] -> a single-node BST with value 0
        
