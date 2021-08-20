"""
- bitwise operation
- O(n), O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        """
        For each unique num:
        - 1st appearance: seen_once - 1 seen_twice - 0  ~seen_twice <1> & (seen_once <0> ^ num <1>) => 1; ~seen_once<0> & (seen_twice ^ num) => 0
        - 2nd appearance: seen_once - 0 seen_twice - 1  ~seen_twice <1> & (seen_once <1> ^ num <1>) => 0; ~seen_once<1> & (seen_twice <0> ^ num <1>) => 1
        - 3rd appearance: seen_once - 0 seen_twice - 0  ~seen_twice <0> & (seen_once ^ num) => 0; ~seen_once<1> & (seen_twice <1> ^ num <1>) => 0
        """
        
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once