"""
- hashmap with linear search
- O(mn), O(m)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        indexes = {n: i for i, n in enumerate(nums2)}
        result = [-1] * n1
        for i1 in range(n1):
            num1 = nums1[i1]
            i2 = indexes[num1] + 1
            while i2 < n2:
                if nums2[i2] > num1:
                    result[i1] = nums2[i2]
                    break
                i2 += 1
        return result

"""
- hashmap + monotonically increase stack
- O(m + n), O(n)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greaters = {}
        mono_increasing_stack = []
        for n in nums2:
            while mono_increasing_stack and n > mono_increasing_stack[-1]:
                greaters[mono_increasing_stack.pop()] = n
            mono_increasing_stack.append(n)
            
        result = []
        for n in nums1:
            result.append(greaters.get(n, -1))
        return result