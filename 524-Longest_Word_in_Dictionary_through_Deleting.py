class Solution:

    """
    - two pointers + sort
    - O(nlogn + mn), O(logn) m - average string length
    """
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        def isSubsequence(word):
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            return i == len(word)
            
        dictionary.sort(key = lambda x: (-len(x), x))
        for word in dictionary:
            if isSubsequence(word):
                return word
        return ""
    
    """
    - two pointers
    - O(mn), O(max_strlen) m - average string length
    """
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        def is_subsequence(word):
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            return i == len(word)
        
        def is_higher_rank(word1, word2):
            if len(word1) == len(word2):
                return word1 < word2
            else:
                return True if len(word1) > len(word2) else False
            
        result = ""
        for word in dictionary:
            if is_subsequence(word) and is_higher_rank(word, result):
                result = word
        return result