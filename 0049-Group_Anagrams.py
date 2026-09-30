"""
- hashmap (with char counts)
- O(n*s)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = [0] * 26
        chars_to_str = defaultdict(list)
        for i in range(len(strs)):
            cur_chars = [c for c in chars]
            s = strs[i]
            for c in s:
                cur_chars[ord(c) - ord('a')] += 1
            chars_to_str[tuple(cur_chars)].append(s)
        return chars_to_str.values()

"""
- hashmap (with sorting)
- O(n*slogs)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_to_str = defaultdict(list)
        for i in range(len(strs)):
            s = strs[i]
            chars_to_str[tuple(sorted(s))].append(s)
        return chars_to_str.values()