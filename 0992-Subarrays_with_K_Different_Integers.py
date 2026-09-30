"""
- brute force
- O(n^2), O(n)
- time limit exceeded
"""
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        counter = collections.Counter()
        result = 0
        for r in range(n):
            counter[nums[r]] += 1
            counter_curr = {k: val for k, val in counter.items()}
            for l in range(r + 1):
                if len(counter_curr.keys()) == k:
                    result += 1
                counter_curr[nums[l]] -= 1
                if counter_curr[nums[l]] == 0:
                    del counter_curr[nums[l]]
        return result

"""
- sliding window
- O(n), O(n)
- intuition: subarraysWithAtMostTDistinct(k) - subarraysWithAtMostTDistinct(k - 1), subarraysWithAtMostTDistinct is the same as problem 340.
"""
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def subarraysWithAtMostTDistinct(t):
            counter = collections.Counter()
            count = 0
            l = 0
            for r, c in enumerate(nums):
                counter[c] += 1
                
                while len(counter.keys()) > t:
                    counter[nums[l]] -= 1
                    if counter[nums[l]] == 0:
                        del counter[nums[l]]
                    l += 1
                count += (r - l + 1)
            return count
        
        return subarraysWithAtMostTDistinct(k) - subarraysWithAtMostTDistinct(k - 1)