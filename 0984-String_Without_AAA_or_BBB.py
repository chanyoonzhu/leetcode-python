"""
- greedy
- https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/508543/APPLES-and-BANANAS-solution-(with-picture)
- O(A + B), O(A + B)
"""
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        res = []
        if a > b:
            high_freq, low_freq, high_c, low_c = a, b, 'a', 'b'
        else:
            high_freq, low_freq, high_c, low_c = b, a, 'b', 'a'
            
        res = [high_c + high_c] * (high_freq // 2) + [high_c] * (high_freq % 2) # put all high freq chars, two per group
        
        i = 0
        for _ in range(low_freq): # put all low freq chars, one at a time in a round robin fashion
            if i == len(res):
                i = 0
            res[i] += low_c
            i += 1
            
        return ''.join(res)

"""
- greedy
- my solution
- O(A + B), O(A + B)
"""
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        res = []
        if a > b:
            high_freq, low_freq, high_c, low_c = a, b, 'a', 'b'
        else:
            high_freq, low_freq, high_c, low_c = b, a, 'b', 'a'
        
        res = [high_c + low_c] * low_freq # consume one high_c and one low_c
        high_freq -= low_freq
        i = 0
        while high_freq and i < len(res): # consume rest high_c
            res[i] = high_c + res[i]
            i += 1
            high_freq -= 1
        if high_freq: # don't forget the end
            res.extend([high_c] * high_freq)
            
        return ''.join(res)
        