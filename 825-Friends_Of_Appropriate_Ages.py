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
            # rule 3 can be included by rule 2, so no need to consider
            # rule 2: can send to all age <= itself
            # rule 1: cannot send to age <= 0.5 * age[x] + 7
            # can send = can send by rule 2 - cannot send by rule 1 - itself
            count = find_bisect_right(x_age) - find_bisect_right(x_age * 0.5 + 7) - 1 # easy to miss: -1 -> can't follow self
            if count > 0: # could be smaller than 0 when x is small
                res += count
        return res