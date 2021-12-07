"""
- sort and binary search （with hashmap)
- O(nlogn)
"""
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages = sorted(ages)
        N = len(ages)
        res = 0

        # key: memoize result since array can be long but the number distinct ages is small 
        @lru_cache(None)
        def find_bisect_right(age):
            return bisect.bisect_right(ages, age)
        
        for x_idx in range(N):
            x_age = ages[x_idx]
            count = find_bisect_right(x_age) - find_bisect_right(x_age * 0.5 + 7) - 1 # easy to miss: -1 -> can't follow self
            if count > 0:
                res += count
        return res