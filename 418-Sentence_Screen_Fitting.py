"""
- brute force
- O(r*c), O(1)
- TLE
"""
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        result = 0
        word_i = 0
        N = len(sentence)       
        
        for r in range(rows):
            c = 0
            while c < cols:
                word_len = len(sentence[word_i])
                space_needed = word_len if c == 0 else word_len + 1 # 1 for space
                if space_needed <= cols - c:
                    c += space_needed
                    word_i += 1
                    if word_i == N: 
                        result += 1
                        word_i = 0
                else:
                    c = cols
        return result

"""
- with cache: dp[i] stores the number of words can be fitted in the row if starting with sentence[i]
"""
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        result = 0
        word_i = 0
        N = len(sentence)
        dp = [-1] * N
        total_fitted = 0
        
        for r in range(rows):
            c = 0
            start_word_i = word_i
            if dp[start_word_i] != -1:
                words_fitted = dp[start_word_i]
                word_i = (word_i + words_fitted) % N
            else:
                words_fitted = 0
                start_word_i = word_i
                while c < cols:
                    word_len = len(sentence[word_i])
                    space_needed = word_len if c == 0 else word_len + 1 # 1 for space
                    if space_needed <= cols - c:
                        c += space_needed
                        word_i = (word_i + 1) % N
                        words_fitted += 1
                    else:
                        c = cols
                dp[start_word_i] = words_fitted
            total_fitted += dp[start_word_i]
        return total_fitted // N

"""
- print multiple words at a time, "taken" stores total space taken so far
- https://leetcode.com/problems/sentence-screen-fitting/discuss/90842/9-lines-in-Python
- O(r*max(word)), O(n)
"""
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        taken, l = 0, len(s)
        for i in range(rows):
            taken += cols # greedily take all spaces in a row
            while s[taken % l] != ' ': # moves a space if can not consume a full word
                taken -= 1
            taken += 1
        return taken // l