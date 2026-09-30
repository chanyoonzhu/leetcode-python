class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        - O(n), O(n)
        
        cnt = collections.Counter(nums)
        for n, c in cnt.items():
            if c > len(nums) / 2:
                return n
        """
        
        """
        Moore's Voting
        """
        count, candidate = 0, 0
        for n in nums:
            if count == 0:
                candidate = n
                count += 1
            else:
                if n == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate
            
        
        