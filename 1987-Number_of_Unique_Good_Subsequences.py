"""
- brute force
- MLE
"""
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        
        all_good = set([""])
        MOD = 10 ** 9 + 7
    
        for bit in binary:
            new_good = set()
            for seq in all_good:
                if seq != "0":
                    new_good.add(seq + bit)
            all_good |= new_good
        return (len(all_good) - 1) % MOD

"""
- better brute force
- TLE
"""
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        
        all_good = set([0])
        has_zero = False
        MOD = 10 ** 9 + 7
    
        for bitstr in binary:
            if bitstr == "0": has_zero = True
            new_good = set()
            for bit in all_good:
                new_good.add((bit << 1) + (1 if bitstr == "1" else 0))
            all_good |= new_good
        return (len(all_good) - (1 if not has_zero else 0)) % MOD

"""
- same: 940-Distinct Subsequences II
- TLE
"""
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        
        MOD = 10 ** 9 + 7

        dp = [1 if bit == "1" else 0 for bit in binary]
        first_one = binary.find("1")
        if first_one == -1:
            first_one = len(dp)

        for i in range(first_one + 1, len(dp)):
            for k in range(first_one, i):
                if binary[i] != binary[k]:
                    dp[i] = (dp[i] + dp[k]) % MOD
        return (sum(dp[first_one:]) + (1 if "0" in binary else 0)) % MOD

"""
- todo: https://leetcode.com/problems/number-of-unique-good-subsequences/discuss/1432051/DP-O(n)-or-O(1)
"""
        