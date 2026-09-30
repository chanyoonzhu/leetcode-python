"""
- monotonically decreasing/increasing stack
- O(n), O(n)
- intuition: think in reverse - pin a number, find the longest subarray that this number is the min, count sums of this subarray
    for any number x, if it has l consecutive elements larger than itself on its left and r on its right, the the number of subarrays with x being the smallest is l * r
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        MOD = 10 ** 9 + 7
        left_larger_counts, right_larger_counts = [0] * N, [0] * N # number of (connected) larger numbers on left/right of i
        stack_l, stack_r = [], [] # mono-increasing stack: (i, larger_count)
        
        for i, x in enumerate(arr):
            left_larger = 1
            while stack_l and arr[stack_l[-1][0]] >= x:
                left_larger += stack_l.pop()[1] # key: accumulated
            stack_l.append((i, left_larger))
            left_larger_counts[i] = left_larger
        
        for i in range(N-1, -1, -1):
            x = arr[i]
            right_larger = 1
            while stack_r and arr[stack_r[-1][0]] > x: # caveat: don't use "==" in stack_r to avoid calculating twice when continuous numbers are equal
                right_larger += stack_r.pop()[1]
            stack_r.append((i, right_larger))
            right_larger_counts[i] = right_larger
            
        return sum(x * left_larger * right_larger for x, left_larger, right_larger in zip(arr, left_larger_counts, right_larger_counts)) % MOD