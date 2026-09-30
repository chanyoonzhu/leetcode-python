class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1 = pos2 = -1
        result = len(wordsDict)
        for i, w in enumerate(wordsDict):
            if w == word1:
                pos1 = i
            elif w == word2:
                pos2 = i
            if pos1 >= 0 and pos2 >= 0:
                result = min(result, abs(pos2 - pos1))
        return result