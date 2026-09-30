"""
- reverse the whole integer and compare
- O(log10(n)), O(1)
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # easy to miss
            return False
        x_reversed = 0
        x_copy = x
        while x_copy:
            div, mod = divmod(x_copy, 10)
            x_copy = div
            x_reversed = x_reversed * 10 + mod
        
        return x_reversed == x

"""
- optimized reverse half of the integer and compare
- O(log10(n)), O(1)
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0): # easy to miss: edge case
            return False
        x_reversed = 0
        x_copy = x
        while x_copy > x_reversed:
            div, mod = divmod(x_copy, 10)
            x_copy = div
            x_reversed = x_reversed * 10 + mod
        
        return x_copy == x_reversed or x_copy == x_reversed // 10 # for odd