"""
- string
- O(n), O(1)
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word = word + "a"
        abbr = abbr + "a" # dummy, handles the case when the end letter is a digit
        
        word_len = len(word)
        word_i = 0
        count = 0
        for c in abbr:
            if not c.isdigit():
                if count:
                    word_i += count
                    if word_i >= word_len:
                        return False
                    count = 0
                if word_i >= word_len or c != word[word_i]:
                    return False
                word_i += 1
            else:
                n = ord(c) - ord('0')
                if not count and not n: # leading 0
                    return False
                count = count * 10 + n
        return word_i == word_len

"""
- two pointers
- O(n), O(1)
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ptr1 = ptr2 = 0
        n1, n2 = len(word), len(abbr)
        sublen = 0
        while ptr1 < n1: # consume word
            if sublen > 0: # consume numbers
                sublen -= 1
                ptr1 += 1
            elif ptr2 == n2: # completes abbr before word is fully consumed
                return False
            else: # ptr2 < n2, sublen = 0
                if not abbr[ptr2].isdigit():
                    if word[ptr1] != abbr[ptr2]:
                        return False
                    ptr1 += 1
                    ptr2 += 1
                    sublen = 0
                else: # not digit
                    ptr2_start = ptr2
                    while ptr2 < n2 and abbr[ptr2].isdigit():
                        ptr2 += 1
                    sublen = int(abbr[ptr2_start:ptr2])
                    if abbr[ptr2_start] == "0": # easy to miss
                        return False
        return ptr2 == n2 and sublen == 0 # abbr must be all consumed