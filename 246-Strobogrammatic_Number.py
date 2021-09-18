"""
- hashmap with recusion
- O(n), O(n)
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        N = len(num)
        
        # space can be further saved using two pointers
        def helper(i):
            if i >= ceil(N / 2): return True
            if num[i] not in mapping or mapping[num[i]] != num[N - 1 - i]:
                return False
            return helper(i + 1)
        
        return helper(0)