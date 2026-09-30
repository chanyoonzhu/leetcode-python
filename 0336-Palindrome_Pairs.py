from collections import defaultdict

class Trie:
    def __init__(self, idx=-1):
        self.children = defaultdict(Trie)
        self.idx = idx
        self.palindroms_below = list() # smart!
    
    def add(self, word, word_idx):
        node = self
        word = word[::-1] # words have to be inserted in reverse
        for i, c in enumerate(word):
            if word[i:] == word[i:][::-1]:
                node.palindroms_below.append(word_idx)
            node = node.children[c]
        node.idx = word_idx
    
    def findPalindromPair(self, word, word_index):
        node = self
        palindrom_pairs = []
        for i, c in enumerate(word):
            if node.idx != -1 and word[i:] == word[i:][::-1]:
                palindrom_pairs.append((word_index, node.idx))
            if c not in node.children:
                return palindrom_pairs
            node = node.children[c]
        if node.idx != -1 and word_index != node.idx:
            palindrom_pairs.append((word_index, node.idx))
        for p in node.palindroms_below:
            if p != word_index:
                palindrom_pairs.append((word_index, p))
        return palindrom_pairs
        
    def is_palindrom(self, word): # in Python, can use word == word[::-1] which is faster
        if len(word) == 1 or len(word) == 0:
            return True
        if word[0] != word[-1]:
            return False 
        return self.is_palindrom(word[1:-1])          


"""
- Clarification Questions:
Q: Can a word pair up with itself? 
A: No
Q: Is each word unique? 
A: Yes
"""
"""
Additional Discussion: Online Algorithms

This section is beyond what is needed for an interview, and is included only for interest.

When developing algorithms for the real world, an often desirable property is that the algorithm works online. This does not mean on the internet, instead it means that the algorithm can still work if the input data is provided bit-by-bit. In this case, it'd be that we want to feed the algorithm the words one at a time, and each time, we want to update the list of all pairs without doing too much extra work.

So, let's think through how this would work for approach 2. We'd simply be maintaining a hash table of words to indexes. Each time a new word arrives, we'd need to add it to the hash table and also check which existing words it'd form a palindrome pair with. It's a little bit different to before, because we need to find all pairs with previous words that

For case 1, this is straightforward. We simply check if its reverse is already in the hash table. If it is, then we have 2 new pairs (the new word can be either first or second).

But it breaks for case 2 and case 3. It's straightforward to find pairs where our new word is the longer word of the pair (i.e. second in case 2 and first in case 3), however not where the new word is shorter. The problem is that the additional letters of the longer word could be anything, and therefore we have no way of knowing what to look up in the index. Approach 2 worked as an offline algorithm because pairs were always identified by starting with their longer word, and then looking up their shorter word. Going the other way is intractable.

Approach 3, however, works differently. If we build up a Trie as we go, we can always identify words from the Trie that will form the second half of the pair. It doesn't matter whether it is the current word, or the word from the Trie, that is longer. This solves half the problem—each time we get a new word, we can efficiently find all "second" words for it.

We aren't done yet though—the algorithm wouldn't find pairs where our current word was second. We still need to find a way of identifying all "first" words for the current word. It turns out that if we hadn't reversed words when putting them into the Trie, but instead had reversed the word we are looking up, that we'd be looking up "first" words in the Trie.

Therefore, we can make an online algorithm by maintaining 2 Tries—one with the words forward, and one with the words in reverse. The reverse Trie tells us where the new word will be the first word of a pair, and the forward Trie tells us where the new word will be the second of a pair.
"""
class Solution:
    """
    - Trie
    - Time: O(k^2*n) - k is the length of the longest word; Space: O(k*n^2) worst case, 
    each of the O(n*k) letters in the input would be on separate nodes, and each node would have up to n indexes in its list
    """
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        result = []
        for i, word in enumerate(words):
            trie.add(word, i)
        for i, word in enumerate(words):
            result.extend(trie.findPalindromPair(word, i))
        return result
    
    """
    - Hashmap
    - Time: O(k^2*n), Space: O((k+n)^2) - input O(kn), hashmap O(kn), lookup O(k^2), output O(n^2)
    """
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_index = dict()
        result = []
        for i, word in enumerate(words):
            word_to_index[word] = i
        for i, word in enumerate(words):
            for j in range(len(word) + 1): # j = len(word) allows for cases like ("a", "")
                reversed_part = word[:j][::-1]
                if reversed_part in word_to_index and word[j:] == word[j:][::-1]:
                    if word_to_index[reversed_part] != i:
                        result.append((i, word_to_index[reversed_part]))
                reversed_part = word[j:][::-1]
                if j != 0 and reversed_part in word_to_index and word[:j] == word[:j][::-1]: # j ！= 0 avoids adding the same pair when j = len(word)
                    if word_to_index[reversed_part] != i:
                        result.append((word_to_index[reversed_part], i))
        return result
        
s = Solution()
ans = s.palindromePairs(["lls","s","sssll"])
print(ans)