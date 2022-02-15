"""
- dp (my solution, not very efficient)
"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mem = {} # stores words already computed
        N = len(s)
        result = 0
        
        def helper(w):
            nonlocal N
            if not w: return -1
            if w not in mem:
                prev_end = helper(w[:-1])
                i = s.find(w[-1], prev_end + 1, N)
                mem[w] = i if i != -1 else N
            return mem[w]
        
        for word in words:
            if helper(word) != N:
                result += 1
        return result

"""
- hashmap + binary search
"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexes = collections.defaultdict(list)
        result = 0
        N = len(s)
        for i, c in enumerate(s):
            indexes[c].append(i)
        for w in words:
            c_index_prev = -1
            not_matching = False
            for c in w:
                i = bisect.bisect_left(indexes[c], c_index_prev + 1) # get char index in s
                if i == len(indexes[c]) or indexes[c][i] <= c_index_prev:  # char index in s must be larger than previous char index in s
                    not_matching = True
                    break
                c_index_prev = indexes[c][i]
            if not not_matching: result += 1 
        return result

"""
- hashmap
- use a map to track - key: current char in s: remaining part of words that start with that char
- smart solution!
"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = collections.defaultdict(list) # stores subsequence left to be consumed
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in s: # greedily consume as many subsequence in all words
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count