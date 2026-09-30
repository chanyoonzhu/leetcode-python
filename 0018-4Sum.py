"""
- two pointers
- O(n^3)
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-1, 2, -1):
            if i < n-1 and nums[i] == nums[i+1]: # dedup
                    continue
            for j in range(i-2):
                if j > 0 and nums[j] == nums[j-1]: # dedup
                    continue
                two_sum = nums[i] + nums[j]
                other_twos = self.twoSum(nums, j+1, i-1, target - two_sum)
                for first, second in other_twos:
                    res.append([nums[j], first, second, nums[i]])
        return res
        
    def twoSum(self, nums, start, end, target):
        i, j = start, end
        res = []
        while i < j:
            two_sum = nums[i] + nums[j]
            if two_sum == target:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif two_sum < target:
                i += 1
            else:
                j -= 1
            # dedup
            while start < i <= j and nums[i] == nums[i-1]: 
                i += 1
            while  i <= j < end and nums[j] == nums[j+1]:
                j -= 1
        return res