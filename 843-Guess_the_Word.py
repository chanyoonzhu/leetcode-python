# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

"""
- greedy
- greedily test the word that overlaps with most other candidate words, once find the number of matches of that "most popular" word, can filter out incorrect words counting the matches between candidate words and the "most popular" word 
"""
class Solution:
    def findSecretWord(self, wordlist: list[str], master) -> None:
        def pair_matches(a, b):
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            counts = [[0 for _ in range(26)] for _ in range(6)] # counts[i][j] is nb of words with char j at index i
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord("a")] += 1

            best_score = 0
            for word in candidates:
                score = 0
                for i, c in enumerate(word):
                    score += counts[i][ord(c) - ord("a")]
                if score > best_score:
                    best_score = score
                    best_word = word

            return best_word

        candidates = wordlist[:]
        while candidates:

            s = most_overlap_word() # guess the word that overlaps with most others
            matches = master.guess(s)

            if matches == 6:
                return

            candidates = [w for w in candidates if pair_matches(s, w) == matches] # filter out incorrect guess using "matches"

s = Solution()
print(s.findSecretWord(["acckzz","ccbazz","eiowzz","abcczz"], None))