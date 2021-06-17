"""
- greedy: start from the smallest element(since only the smaller will be used in the next product, can use greedy instead of dynamic programming)
- O(n^2), O(n)
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        result = 0
        while len(arr) > 1:
            min_idx = arr.index(min(arr))
            if 0 < min_idx < len(arr) - 1:
                result += min(arr[min_idx - 1], arr[min_idx + 1]) * arr[min_idx]
            else:
                result += arr[1 if min_idx == 0 else min_idx - 1] * arr[min_idx]
            arr.pop(min_idx)
        return result

"""
- monotonically decreasing stack
- O(n), O(n)
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        result = 0
        stack = [float('inf')]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop() # regional dip
                result += mid * min(stack[-1], a) # min of left and right
            stack.append(a)
        while len(stack) > 2:
            result += stack.pop() * stack[-1]
        return result