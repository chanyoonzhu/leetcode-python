"""
- monotonically decreasing/increasing stack
- O(n), O(n)
- intuition: think in reverse - pin a number, find the longest subarray that this number is the min, count sums of this subarray
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n, mod = len(arr), 10 ** 9 + 7
        left, right, s_left, s_right = [0] * n, [0] * n, [], []
        for i in range(n):
            a, larger_count = arr[i], 1
            while s_left and s_left[-1][0] > a:
                larger_count += s_left.pop()[1]
            left[i] = larger_count
            s_left.append((a, larger_count))
        
        for i in range(n - 1, -1, -1):
            a, larger_count = arr[i], 1
            while s_right and s_right[-1][0] >= a: # caveat: use >= in s_right but > in l_right to dedup when numbers are equal
                larger_count += s_right.pop()[1]
            right[i] = larger_count
            s_right.append((a, larger_count))
        
        return sum(a * larger_count_left * larger_count_right for a, larger_count_left, larger_count_right in zip(arr, left, right)) % mod