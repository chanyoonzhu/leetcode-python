"""
- bucket sort
- O(n), O(n)
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        buckets = {}
        for i, x in enumerate(nums):
            bucket_id = x // t if t else x # easy to miss t == 0
            
            # check existence
            if bucket_id in buckets: return True
            if bucket_id - 1 in buckets and abs(x - nums[buckets[bucket_id - 1]]) <= t: return True
            if bucket_id + 1 in buckets and abs(x - nums[buckets[bucket_id + 1]]) <= t: return True
            
            # update bucket
            buckets[bucket_id] = i
            # remove out of range items (easy to miss)
            if i >= k:
                expired_bucket_id = nums[i - k] // t if t != 0 else nums[i - k]
                del buckets[expired_bucket_id]
        
        return False

"""
- SortList
- O(nlogk), O(nlogk)
"""
from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
                
        sorted_list = SortedList()
        for i, x in enumerate(nums): 
            if i > k: sorted_list.remove(nums[i-k-1]) 
                
            # check if current sliding window contains a number in range [nums[i] - t, nums[i] + t]
            pos1 = SortedList.bisect_left(sorted_list, x - t)
            pos2 = SortedList.bisect_right(sorted_list, x + t)
            if pos2 > pos1: return True
            
            sorted_list.add(nums[i])
        
        return False