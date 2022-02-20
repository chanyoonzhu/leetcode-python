"""
- prefix sum
"""
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        # min_till[i] - minimum subarray length with target sum seen at and before i
        min_till = [float("inf")] * len(arr)
        prefixe_sum = 0
        prefix_to_last_idx = {0: -1}
        res = float("inf")

        for i, x in enumerate(arr):
            min_till[i] = min_till[i-1]
            prefixe_sum += x
            if prefixe_sum - target in prefix_to_last_idx:
                left_i = prefix_to_last_idx[prefixe_sum - target]
                res = min(res, (min_till[left_i] if left_i >= 0 else float("inf")) + i - left_i)
                min_till[i] = min(min_till[i], i - left_i)
            prefix_to_last_idx[prefixe_sum] = i
        return res if res < float("inf") else -1