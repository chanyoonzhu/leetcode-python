class Solution:
    """
    - two-pointers with hashmap - put the squares in hashmap
    - O(m^2 + n^2), O(m + n)
    """
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dict1, dict2 = collections.Counter([num * num for num in nums1]), collections.Counter([num * num for num in nums2])
        self.total = 0
        
        def helper(square_dict, nums):
            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    product = nums[i] * nums[j]
                    if product in square_dict:
                        self.total += square_dict[product]
        
        helper(dict1, nums2)
        helper(dict2, nums1)
        
        return self.total

    """
    - two-pointers with hashmap - put the numbers in hashmap
    - O(m*n), O(m + n)
    """
     def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
           
        def helper(target, nums):
            total = 0
            seen = collections.Counter()
            for num in nums:
                div, mod = divmod(target, num)
                if mod == 0 and div in seen:
                    total += seen[div]
                seen[num] += 1
            return total
        
        return sum(helper(num * num, nums2) for num in nums1) + sum(helper(num * num, nums1) for num in nums2)
    
    """
    - two-pointers with hashmap - put the numbers in hashmap - optimized with cache
    - O(m*n), O(m + n)
    """
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
           
        def helper(target, nums):
            total = 0
            seen = collections.Counter()
            for num in nums:
                div, mod = divmod(target, num)
                if mod == 0 and div in seen:
                    total += seen[div]
                seen[num] += 1
            return total
    
        @lru_cache(None)
        def target_1(target):
            return helper(target, nums2)
        
        @lru_cache(None)
        def target_2(target):
            return helper(target, nums1)
        
        return sum(target_1(num * num) for num in nums1) + sum(target_2(num * num) for num in nums2)