# Clarification questions for Word Ladder (127):
# - Must all words have equal length, and must each step change exactly one letter?
#   Yes; that is the problem's transformation rule and word-length constraint.
# - Must endWord appear in wordList? Yes; otherwise return 0. beginWord need not appear.
# - Must every intermediate word come from wordList? Yes; beginWord is the exception.
# - Does the sequence length count words or transformations? It counts words,
#   including beginWord and endWord.
# - Is the requested output the shortest length or the actual sequence? The
#   problem asks for the length only.
# - Can wordList be empty or contain duplicates? The constraints require a
#   non-empty list of unique words; this implementation still handles empty input.
# - Can beginWord equal endWord? The general interpretation used here returns 1.
# - Which characters are allowed, and how large can wordList be? Lowercase
#   English letters; up to 5,000 words, which makes the full-list scan costly.

import collections
from collections import deque
from typing import List


class Solution:
    """Updated September 2026: BFS using generated one-letter substitutions.

    Complexity:
        Time: O(W * L^2), where W is the number of words and L their length.
        Space: O(W * L) for generated words retained by the queue and visited set.
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_queue = deque()
        word_queue.append((beginWord, 1))
        visited = set()
        all_words = set(wordList)
        ord_a = ord('a')

        while word_queue:
            word, steps = word_queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in [chr(ord_a + ci) for ci in range(26)]:
                    linked_word = word[:i] + c + word[i + 1:]
                    if linked_word in all_words and linked_word not in visited:
                        word_queue.append((linked_word, steps + 1))
                        visited.add(linked_word)

        return 0

"""BFS that removes discovered words from the set.

Complexity:
    Time: O(W * L^2) worst case, including string generation and hashing.
    Space: O(W * L) for generated words retained by the queue.
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


"""bidirectional BFS using generated substitutions.

Complexity:
    Time: O(W * L^2) worst case; bidirectional search often explores fewer words.
    Space: O(W * L) for generated words retained by the search frontiers.
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


class Solution:
    """Added September 2026: intentionally inefficient BFS that scans wordList for
    every position of every dequeued word. This version is expected to time out.

    Why it exceeds the time limit:
        For each of up to W visited words, it scans all W candidates at each of
        L character positions. Prefix and suffix slicing/comparison costs O(L),
        giving O(W^2 * L^2) time in the worst case. With W up to 5,000, this
        repeats far more work than generating and looking up one-letter changes.

    Complexity:
        Time: O(W^2 * L^2), where W = len(wordList) and L = len(beginWord).
        Space: O(W) for the visited set and BFS queue (excluding the input list).
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while word_queue:
            word, steps = word_queue.popleft()
            if word == endWord:
                return steps

            for index in range(len(word)):
                for candidate in wordList:
                    if len(candidate) != len(word) or candidate in visited:
                        continue
                    if (
                        word[:index] == candidate[:index]
                        and word[index + 1:] == candidate[index + 1:]
                        and word[index] != candidate[index]
                    ):
                        visited.add(candidate)
                        word_queue.append((candidate, steps + 1))

        return 0


# Interview test cases for Word Ladder (127), grouped by behavior:
# Core transformation:
#   - hit -> cog through [hot, dot, dog, lot, log, cog] -> 5 words.
#   - hit -> hot through [hot] -> 2 words (one transformation).
# Unreachable and missing targets:
#   - endWord absent from wordList -> 0.
#   - No valid chain between beginWord and endWord -> 0.
# Boundaries and input details:
#   - beginWord == endWord -> 1 under the documented general interpretation.
#   - Empty wordList with different endpoints -> 0 (defensive case).
#   - Duplicate entries in wordList do not change the shortest sequence.
# Performance:
#   - A large wordList demonstrates repeated full-list scans and substring
#     comparisons that make this intentionally naive implementation time out.
