"""
- backtracking
https://leetcode.com/problems/verbal-arithmetic-puzzle/discuss/463920/Python-Backtracking
"""
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        words.append(result)
        N, maxWordN = len(words), max(map(len, words))

        mapping = {}
        assigned = set()

        def backtrack(col, word_i, carry):
            if col >= maxWordN:
                return carry == 0
            if word_i == N:
                return carry % 10 == 0 and backtrack(col + 1, 0, carry // 10)

            word = words[word_i]
            if col >= len(word):
                return backtrack(col, word_i + 1, carry)

            letter = word[~col]
            sign = 1 if word_i < N - 1 else -1
            if letter in mapping:
                if (mapping[letter] or col != len(word) - 1): # leading zero check
                    return backtrack(col, word_i + 1, carry + sign * mapping[letter])
                return False
            else:
                for d in range(10):
                    if d not in assigned and (d or len(word) == 1 or col != len(word) - 1):
                        assigned.add(d)
                        mapping[letter] = d
                        if backtrack(col, word_i + 1, carry + sign * d):
                            return True
                        assigned.remove(d)
                        del mapping[letter]
            return False
            
        return backtrack(0, 0, 0)
        
            