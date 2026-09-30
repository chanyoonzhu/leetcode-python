"""
- sort
- O(logn), O(logn)
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        N = len(digits)
        l = r = -1
        
        # l - first element from right that breaks the increasing sequence
        for i in range(N - 1, 0, -1):
            if ord(digits[i]) > ord(digits[i-1]):
                l = i - 1
                break
        if l == -1: # no larger element
            return -1
        
        # r - first element just larger than digit at index l
        r = l + 1
        while r < N and ord(digits[r]) > ord(digits[l]):
            r += 1
        r -= 1
                
        digits[l], digits[r] = digits[r], digits[l]
        self.reverse(digits, l + 1, N - 1)
        
        res = int(''.join(digits))
        return res if res < 1<<31 else -1
    
    def reverse(self, digits, l, r):
        while l < r:
            digits[l], digits[r] = digits[r], digits[l]
            l += 1
            r -= 1        