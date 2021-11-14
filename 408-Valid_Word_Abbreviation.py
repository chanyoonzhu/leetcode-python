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