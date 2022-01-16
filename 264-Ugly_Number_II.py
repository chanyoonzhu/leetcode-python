"""
- dp - knapsack
- intuition: https://leetcode.com/problems/ugly-number-ii/discuss/69384/My-expressive-Python-solution/268546
- O(logn), O(n)
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1]
        ptrs = [[2, 0], [3, 0], [5, 0]] # (prime, prev ugly comprised of this prime)
        while n > 1:
            ugly_candidates = [p * uglies[idx] for p, idx in ptrs]
            ugly = min(ugly_candidates)
            uglies.append(ugly)
            # caveat: multiple if (instead of if-else) in case a number can be divided by two primes (dedup)
            if ugly == ugly_candidates[0]: # current ugly is 2 multiple
                ptrs[0][1] += 1
            if ugly == ugly_candidates[1]: # current ugly is 3 multiple
                ptrs[1][1] += 1
            if ugly == ugly_candidates[2]: # current ugly is 5 multiple
                ptrs[2][1] += 1
            n -= 1
        return uglies[-1]