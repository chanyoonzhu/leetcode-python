"""
- brute force
- O(mn), O(1)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2 = len(nums2)
        res = []
        for num1 in nums1:
            i = 0
            while i < n2:
                if num1 == nums2[i]:
                    break
                i += 1
            i += 1
            while i < n2 and nums2[i] < num1:
                i += 1
            res.append(nums2[i] if i < n2 else -1)
        return res

"""
- hashmap with linear search
- O(mn), O(m)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2 = len(nums2)
        res = []
        num2_to_idx = {x: i for i, x in enumerate(nums2)}
        for num1 in nums1:
            i = num2_to_idx[num1] + 1
            while i < n2 and nums2[i] < num1:
                i += 1
            res.append(nums2[i] if i < n2 else -1)
        return res

"""
- hashmap + monotonically increase stack
- O(m + n), O(n)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        res = []
        stack = [] # mono-decreasing
        
        for x in nums2:
            while stack and x > stack[-1]:
                greater[stack.pop()] = x
            stack.append(x)
        
        for x in nums1:
            res.append(greater.get(x, -1))
        
        return res