"""
- dynamic programming
- O(n^3), O(n^2)
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @lru_cache(None)
        def dp(l, r):
            if l == r: return 0
            total = float("inf")
            for k in range(l + 1, r + 1): # partition the array into two parts
                left = dp(l, k - 1)
                right = dp(k, r)
                max_left = max(arr[i] for i in range(l, k))
                max_right = max(arr[i] for i in range(k, r + 1))
                total = min(total, max_left * max_right + left + right)
            return total
        
        return dp(0, len(arr) - 1)

"""
- greedy: start from the smallest element(since only the smaller will be used in the next product, can use greedy instead of dynamic programming)
- O(n^2), O(n)
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            min_idx = arr.index(min(arr))
            res += min(arr[min_idx - 1] if min_idx > 0 else float("inf"), arr[min_idx + 1] if min_idx < len(arr) - 1 else float("inf")) * arr[min_idx]
            del arr[min_idx]
        return res

"""
- monotonically decreasing stack
- O(n), O(n)
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [] # left candidate
        for a in arr:
            while stack and stack[-1] <= a:
                mid = stack.pop() # mid is regional dip
                if not stack:
                    res += mid * a
                else:
                    res += mid * min(stack[-1], a) # min of left and right
            stack.append(a)
        while len(stack) > 1:
            res += stack.pop() * stack[-1]
        return res