"""
- BFS
- O(n*s), O(n*s)
""" 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        N = len(beginWord)
        ORD_A = ord('a')
        all_words = set(wordList)
        if endWord not in all_words: return 0
        
        q = collections.deque()
        visited = set()
        q.append((beginWord, 1))
        visited.add(beginWord)
        
        while q:
            word, steps = q.popleft()
            if word == endWord: return steps
            for i in range(N):
                for c in [chr(ORD_A + ci) for ci in range(26)]:
                    if c != word[i]:
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in all_words and new_word not in visited:
                            q.append((new_word, steps + 1))
                            visited.add(new_word)
                        
        return 0

"""
- BFS (space optimized: no visited, keep removing visited out of wordList instead)
- O(n*s), O(n*s)
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        N = len(beginWord)
        ORD_A = ord('a')
        all_words = set(wordList)
        if endWord not in all_words: return 0
        
        q = collections.deque()
        q.append((beginWord, 1))
        
        while q:
            word, steps = q.popleft()
            if word == endWord: return steps
            for i in range(N):
                for c in [chr(ORD_A + ci) for ci in range(26)]:
                    if c != word[i]:
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in all_words:
                            q.append((new_word, steps + 1))
                            all_words.remove(new_word)
                        
        return 0


"""
- birectional bfs
- O(n*s), O(n*s)
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        N = len(beginWord)
        ORD_A = ord('a')
        all_words = set(wordList)
        if endWord not in all_words: return 0
        
        words1, words2 = set(), set()
        words1.add(beginWord)
        words2.add(endWord)
        all_words.discard(endWord)
        
        steps = 0
        while words1:
            if len(words1) > len(words2):
                words1, words2 = words2, words1
            new_words = set()
            
            for word in words1:
                for i in range(N):
                    for c in [chr(ORD_A + ci) for ci in range(26)]:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in words2:
                                return steps + 2
                            if new_word in all_words:
                                new_words.add(new_word)
                                all_words.remove(new_word)
            words1 = new_words
            steps += 1
        return 0
        

sl = Solution()
begin = "hit"
end = "cog"
words = ["hot","dot","dog","lot","log","cog"]
print(sl.ladderLength(begin, end, words))