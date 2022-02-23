"""
- sort and convert
- O(mwlogw + nwlogw)
"""
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        res = 0
        all_start_words = self.letterSorted(startWords)
        for target in targetWords:
            for converted in self.reverseConvert(target):
                if converted in all_start_words:
                    print(converted)
                    res += 1
                    break # easy to miss: only needs to find one startWord to pair with target
        return res
    
    def letterSorted(self, startWords):
        all_starts = set()
        for word in startWords:
            all_starts.add(''.join(sorted(list(word))))
        return all_starts
    
    def reverseConvert(self, word):
        converted = set()
        counts = Counter(list(word))
        chars = sorted(list(word))
        for i in range(len(chars)):
            if counts[chars[i]] == 1:
                converted.add(''.join(chars[:i] + chars[i+1:]))
        return converted

"""
- Trie
Step1: Build a Trie for each sorted word in startWords
Step2: For each target word in the targetWords list, we try to check whether a target word with one missing character could be found in the Trie. Note: since each target word could be only counted once, if we found a target word with one missing character is matched, we don't need to check rest of missing character combinations.

Time Comp: O(mw + nw*2) : N:word counts, M:char counts for each word
"""
                
                