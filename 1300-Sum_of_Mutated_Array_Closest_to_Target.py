"""
- binary search + greedy
- O(nlog(max(arr))), O(1)
"""
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        low, high = 1, max(arr) # low: change all, high: change nothing
        
        def get_total(x):
            return sum([min(n, x) for n in arr])
        
        while low < high:
            mid = low + (high - low) // 2
            total = get_total(mid)
            if total == target:
                return mid
            elif total < target:
                low = mid + 1
            else:
                high = mid
        if abs(get_total(low) - target) >= abs(get_total(low - 1) - target):
            return low - 1
        return low

"""
- sort 
- O(nlogn), O(logn)
- https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/discuss/463306/JavaC%2B%2BPython-Just-Sort-O(nlogn)
"""
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse=True)
        arr_max = arr[0]
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
        # all numbers that will be used "as-is" (smaller or equal to the best value) are removed, with target adjusted
        if not arr: return arr_max
        # the best value now equals to the the closest integer to target / len(A), if target / len(A) == 0.5, round down since we need the min
        return int(round((target - 0.01) / len(arr)))