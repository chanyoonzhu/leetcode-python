"""
- hashmap
- O(n), O(n)
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val_to_last_idx = {}
        for i, x in enumerate(nums):
            if x in val_to_last_idx and i - val_to_last_idx[x] <= k:
                return True
            val_to_last_idx[x] = i
        return False