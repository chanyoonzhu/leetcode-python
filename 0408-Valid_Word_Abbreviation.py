"""
- two pointers
- O(n), O(1)
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i1 = i2 = 0
        n1, n2 = len(word), len(abbr)
        sublen = 0
        while i1 < n1 and i2 < n2:
            if abbr[i2].isalpha():
                if word[i1] != abbr[i2]:
                    return False
                i1 += 1
                i2 += 1
            else:
                if abbr[i2] == "0":
                    return False
                sub_len = 0
                while i2 < n2 and abbr[i2].isdigit():
                    sub_len = sub_len * 10 + ord(abbr[i2]) - ord("0")
                    i2 += 1
                i1 += sub_len
        return i1 == n1 and i2 == n2