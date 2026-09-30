"""
- two pointers (greedy)
- intuition: greedily test with max width, move pointer on the side with shorter length
- O(n), O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1, ptr2 = 0, len(height) - 1
        res = 0
        while ptr1 < ptr2:
            res = max(res, (ptr2 - ptr1) * min(height[ptr1], height[ptr2]))
            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
        return res