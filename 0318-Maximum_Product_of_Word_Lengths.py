"""
- hashset
- O(n^2*l), O(n)
"""
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        chars = [set(list(w)) for w in words]
        words_len = [len(w) for w in words]
        result = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if not chars[i].intersection(chars[j]):
                    result = max(result, words_len[i] * words_len[j])
        return result

"""
- bit masking
- O(n^2), O(n)
"""
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        result = 0
        bit_mapping = collections.defaultdict(int) # key: bit representation of chars in a word; value: length(max) of word
        for w in words:
            bitmask = 0
            for c in w:
                bitmask |= 1 << (ord(c) - ord('a'))
            bit_mapping[bitmask] = max(bit_mapping[bitmask], len(w))
        
        for mask1 in bit_mapping:
            for mask2 in bit_mapping:
                if mask1 & mask2 == 0: # no overlapping chars
                    result = max(result, bit_mapping[mask1] * bit_mapping[mask2])
        return result