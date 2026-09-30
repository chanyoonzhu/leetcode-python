"""
- hashset
- O((N−L)L), O((N−L)L)
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        seen = set()
        for i in range(9, len(s)):
            seq = s[i-9:i+1]
            if seq in seen:
                res.add(seq)
            else:
                seen.add(seq)
        return list(res)

"""
- bitmasking (rolling sum)
- O(N-L), O(N-L)
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        if len(s) < 11:
            return []
        
        seen = set()
        ans = set()
        key = 0
        mask = (1 << 20) - 1
        for i in range(10):
            key = (key << 2) + to_int[s[i]]
        seen.add(key)
        
        for i in range(10, len(s)):
            key = ((key << 2) + to_int[s[i]]) & mask
            if key in seen:
                ans.add(s[i - 9:i + 1])
            else:
                seen.add(key)
        return list(ans)