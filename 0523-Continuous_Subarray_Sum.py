"""
- hashmap with prefix-sum
- TLE
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixes = {0: -1}
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            for diff in range(0, sum_ + 1, k):
                if sum_ - diff in prefixes and i - prefixes[sum_ - diff] >= 2:
                    return True
            if sum_ not in prefixes: prefixes[sum_] = i
        return False

"""
- hashmap with prefix-sum
- key: hashmap stores (prefix-sum % k) as key
- O(n), O(n)
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixes = {0: -1}
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ = (sum_ + x) % k
            if sum_ in prefixes and i - prefixes[sum_] >= 2:
                return True
            if sum_ not in prefixes: prefixes[sum_] = i
        return False