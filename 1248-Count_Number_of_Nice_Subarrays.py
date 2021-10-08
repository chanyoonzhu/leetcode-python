"""
- hashmap + prefix sum
- O(n), O(n)
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        memo = collections.Counter()
        memo[0] = 1
        result = odds = 0
        for x in nums:
            if x % 2:
                odds += 1
            memo[odds] += 1
            result += memo[odds - k]
        return result

"""
- sliding window: two pointers
- O(n), O(1)
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    
        left = 0
        result = 0 
        odd_cnt = 0
        cur_sub_cnt = 0
        for x in nums:
            
            if x % 2 == 1:
                odd_cnt += 1
                cur_sub_cnt = 0
                
            while odd_cnt == k:
                cur_sub_cnt += 1
                if nums[left] % 2 == 1:
                    odd_cnt -= 1
                left += 1
                
            result += cur_sub_cnt
            
        return result  