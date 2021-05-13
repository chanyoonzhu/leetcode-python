"""
- two pointers
- O(n^2), O(n)
- time limit exceeded
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = n, 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    l = min(l, i)
                    r = max(r, j)
        return r - l + 1 if r - l > 0 else 0

"""
- sorting
- O(nlogn), O(n)
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums_sorted[l] == nums[l]:
                l += 1
            else:
                break
        if l == r:
            return 0
        
        while nums_sorted[r] == nums[r]:
            r -= 1
            
        return r - l + 1

"""
- two stacks - compute start and end index separately using two stacks
- O(n), O(n)
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        l, r = n, 0
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        
        stack.clear()
        
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        
        return r - l + 1 if r > l else 0

"""
- space optimized
- O(n), O(1)
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        _min, _max = float("inf"), float("-inf") # _min: min value since first time 1st stack pop, _max: max value since first time 2nd stack pop
        
        is_in_order = True
        for i in range(1, n):
            if is_in_order and nums[i] < nums[i - 1]:
                is_in_order = False
            if not is_in_order:
                _min = min(_min, nums[i])
            
        is_in_order = True
        for i in range(n - 2, -1, -1):
            if is_in_order and nums[i] > nums[i + 1]:
                is_in_order = False
            if not is_in_order:
                _max = max(_max, nums[i])
        
        l, r = 0, n - 1
        while l < n:
            if _min < nums[l]: # breaks at the place where _min should be inserted in 1st stack
                break
            l += 1
        while r >= 0:
            if _max > nums[r]: # breaks at the place where _max should be inserted in 2nd stack
                break
            r -= 1
        
        return r - l + 1 if r > l else 0