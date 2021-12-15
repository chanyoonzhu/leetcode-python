"""
- math + two pointers
- O(n), O(n)
"""
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        N = len(nums)
        res = [0] * N
        res_idx = 0 if a < 0 else N - 1 # max on the sides if a > 0 otherwise in the middle
        l, r = 0, N - 1
        
        def quad(x):
            return a * (x ** 2) + b * x + c
        
        while l <= r:
            quad_l = quad(nums[l])
            quad_r = quad(nums[r])
            if a >= 0:
                if quad_l > quad_r:
                    res[res_idx] = quad_l
                    l += 1
                else:
                    res[res_idx] = quad_r
                    r -= 1
                res_idx -= 1
            else:
                if quad_l < quad_r:
                    res[res_idx] = quad_l
                    l += 1
                else:
                    res[res_idx] = quad_r
                    r -= 1
                res_idx += 1

        return res