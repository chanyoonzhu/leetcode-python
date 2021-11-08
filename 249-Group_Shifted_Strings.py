"""
- hashmap
- O(nm), O(nm)
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        encode_to_str = defaultdict(list)
        
        def encode(s):
            key = []
            N = len(s)
            for i in range(1, N):
                key.append((ord(s[i]) - ord(s[i-1])) % 26)
            return tuple(key)
        
        for s in strings:
            encode_to_str[encode(s)].append(s)
            
        return [val for val in encode_to_str.values()]