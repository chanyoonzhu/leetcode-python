"""
- hashtable
- O(n^2), O(n)
- intuition: add one more iteration layer on top of 001-two sum
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indexes = dict()
        result = set() # caveat - no dup
        for i, n in enumerate(nums):
            for j in range(i):
                if -n - nums[j] in indexes:
                    result.add(tuple(sorted([-n - nums[j], nums[j], n]))) # caveat - sort to guarantee there's no dup
                indexes[nums[j]] = j
            indexes.clear()
        return result

"""
- two-pointers with sorting
- O(n^2), O(logn) or O(n) - depends on sorting
- intuition: add one more iteration layer on top of 167-two sum II
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i, n in enumerate(nums):
            l, r = 0, i - 1
            while l < r:
                sum_ = nums[l] + nums[r]
                if sum_ == -n:
                    result.add((nums[l], nums[r], n))
                    l += 1
                    r -= 1
                elif sum_ < -n:
                    l += 1
                else:
                    r -= 1
        return result