"""
- birectional bfs
- O(n*s), O(n*s)
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        ladders = collections.defaultdict(list)
        ladders[beginWord].append([beginWord])
        ladders[endWord].append([endWord])
        
        N = len(beginWord)
        ORD_A = ord('a')
        all_words = set(wordList)
        if endWord not in all_words: return []
        
        words1, words2 = set(), set()
        words1.add(beginWord)
        words2.add(endWord)
        
        def getSeqs(ladders1, ladders2):
            seqs = []
            for seq1 in ladders1:
                for seq2 in ladders2:
                    if seq1[0] == endWord:
                        seq1, seq2 = seq2, seq1
                    seqs.append(seq1 + seq2[::-1])
            return seqs
        
        steps = 0
        result = []
        found = False
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
                                result.extend(getSeqs(ladders[word], ladders[new_word]))
                                found = True
                            if new_word in all_words:
                                new_words.add(new_word)
                                ladders[new_word].extend([ladder + [new_word] for ladder in ladders[word]])
                del ladders[word]
            if found: break
            words1 = new_words
            all_words -= new_words
            steps += 1
        return result