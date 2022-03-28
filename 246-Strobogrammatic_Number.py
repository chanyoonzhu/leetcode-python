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

"""
- hashmap with two pointers
- O(n), O(n)
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        N = len(num)
        
        l, r = 0, len(num) - 1
        while l <= r: # easy to miss: "=" for edge case like "2"
            if num[l] not in mapping or mapping[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True
        
