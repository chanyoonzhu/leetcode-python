"""
- bitwise operations
- intuition: when multiplication and division cannot be used, we can use addition and subtraction. Linear subtraction is slow, can subtract power
- eg: (remaining dividend, substract_count): (20, 0) -> (20 - 2 ^ 0 * 3 = 17, 1) -> (17 - 2 ^ 1 * 3=11, 3) -> (11 - 2 ^ 2 * 3 = -1, 3)cannot be neg, reset power -> (11 - 2 ^ 0 * 3 = 8, 4) -> (8 - 2 ^ 1 * 3 = 2, 5)
- O(log(divide / divisor)), O(1)
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        
        same_sign = (dividend > 0) == (divisor > 0) # caveat: can be negative
        dividend, divisor = abs(dividend), abs(divisor)
        
        while dividend >= divisor:
            cur_divisor, subtract_count = divisor, 1
            while dividend >= cur_divisor:
                dividend -= cur_divisor
                result += subtract_count
                cur_divisor <<= 1
                subtract_count <<= 1
            
        if not same_sign:
            result = -result
        return min(max(-2**31, result), 2**31 - 1) # caveat: overflow