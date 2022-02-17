"""
- brute force
- O(nmm) - n: number of words, m - word length
"""
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        pool = set()
        for c_i in range(len(dict[0])):
            for w_i in range(len(dict)):
                removed = dict[w_i][:c_i] + "_" + dict[w_i][c_i+1:]
                if removed in pool:
                    return True
                pool.add(removed)
            pool = set()
        return False

"""
- string hashing
- O(nm)
"""
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        MOD = 10 ** 11 + 7 # collisions can happen
        M = len(dict[0])
        pool = set()
        hashed = [self.hashStr(s) for s in dict] # precompute string hashes
        for c_i in range(M):
            for w_i in range(len(dict)):
                removed = hashed[w_i] - self.hashCharAtIndex(dict[w_i][c_i], M - 1 - c_i) # removed hash is original hash minus hash of the removed
                if removed in pool:
                    return True
                pool.add(removed)
            pool = set()
        return False
    
    def hashStr(self, s):
        MOD = 10 ** 11 + 7
        hashed = 0
        for i in range(len(s)):
            hashed = (hashed * 26 + ord(s[i]) - ord('a')) % MOD
        return hashed
    
    def hashCharAtIndex(self, c, idx):
        MOD = 10 ** 11 + 7
        hashed = ord(c) - ord('a')
        for _ in range(idx):
            hashed = hashed * 26 % MOD
        return hashed
        