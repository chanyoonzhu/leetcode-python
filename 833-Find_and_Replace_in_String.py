"""
- string
"""
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        S = list(s)
        
        for idx, source, target in sorted(zip(indices, sources, targets), reverse=True): # replace larger index first
            if s[idx:idx+len(source)] == source:
                S[idx:idx+len(source)] = list(target)
        
        return "".join(S)