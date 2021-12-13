"""
- two pointers
- init: O(n), O(n); shortest: O(m1 + m2) m1/m2: number of times word1/2 shows up in dict, O(m1+m2)
"""
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_indexes = self._getWordToIndexes(wordsDict)
        self.memo = {}
        
    def _getWordToIndexes(self, wordsDict: List[str]):
        word_indexes = defaultdict(list)
        for i, w in enumerate(wordsDict):
            word_indexes[w].append(i)
        return word_indexes

    def shortest(self, word1: str, word2: str) -> int:
        if word1 > word2:
            word1, word2 = word2, word1
        if (word1, word2) not in self.memo:
            indexes_word1 = self.word_indexes[word1]
            indexes_word2 = self.word_indexes[word2]
            p1 = p2 = 0
            res = float("inf")
            while p1 < len(indexes_word1) and p2 < len(indexes_word2):
                res = min(res, abs(indexes_word1[p1] - indexes_word2[p2]))
                if indexes_word1[p1] == indexes_word2[p2]:
                    self.memo[(word1, word2)] = 0
                    return 0
                elif indexes_word1[p1] > indexes_word2[p2]:
                    p2 += 1
                else:
                    p1 += 1
            self.memo[(word1, word2)] = res
        return self.memo[(word1, word2)]