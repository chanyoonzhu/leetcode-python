"""
Clarification Questions:
Q: What if one interval start time is the end time of another interval?
A: Also needs to be logged, eg. [5, 5]
"""
class Solution(object):
    """
    - Two-pointers
    - O(m+n), O(m+n)
    """
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ptr_A = ptr_B = 0
        res = []
        while ptr_A < len(A) and ptr_B < len(B):
            a_start, a_end = A[ptr_A]
            b_start, b_end = B[ptr_B]
            max_start, min_end = max(a_start, b_start), min(a_end, b_end)
            if min_end >= max_start:
                res.append([max_start, min_end])
            if b_end > a_end:
                ptr_A += 1
            else:
                ptr_B += 1
        return res