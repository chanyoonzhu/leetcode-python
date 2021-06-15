"""
- prefix sum + sliding window
- O(n^2), O(n)
- time limit exceeded
"""
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefixes = [0]
        for num in nums:
            prefixes.append(prefixes[-1] + num)
            
        result = 0
        for i in range(n):
            _min = nums[i]
            for j in range(i, n):
                _min = min(_min, nums[j])
                result = max(result, _min * (prefixes[j + 1] - prefixes[i]))
        return result % (10 ** 9 + 7)

"""
- monotonically increasing stack - finds the l/r boundaries of nums[i] (indexes j in boundaries satisfies nums[j] >= nums[i])
- O(n), O(n)
"""
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        stack = []
        l_bounds, r_bounds = [0] * n, [0] * n
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            l_bounds[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            r_bounds[i] = stack[-1] - 1 if stack else n - 1
            stack.append(i)
            
        
        prefixes = [0]
        for num in nums:
            prefixes.append(prefixes[-1] + num)
          
        result = 0
        for i in range(n):
            l, r = l_bounds[i], r_bounds[i]
            result = max(result, nums[i] * (prefixes[r + 1] - prefixes[l]))
        
        return result % (10 ** 9 + 7)

"""
- similar problem: 84-Largest Rectangle in Histogram (convert width to sum)
- monotonically increasing stack - finds the l/r boundaries of nums[i] (indexes j in boundaries satisfies nums[j] >= nums[i])
- O(n), O(n)
"""
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        nums = nums + [-1] 
        stack = [0]
        result = 0
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1]+n)
            
        for i in range(1, len(nums)): # i is the right boundary
            while nums[i] < nums[stack[-1]]:
                height = nums[stack.pop()]
                _sum = prefix[i] - prefix[stack[-1] + 1] # stack[-1] is the left boundary
                result = max(result, _sum * height)
            stack.append(i)
        return result % (10 ** 9 + 7)