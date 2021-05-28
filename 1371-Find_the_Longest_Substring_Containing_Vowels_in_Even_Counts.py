"""
- two pointers with hashset
- O(n^2), O(n)
- time limit exceeded
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        odd_vowels = set([])
        result = 0
        
        def track_odd_vowels(odd_vowels, c):
            if c in ['a', 'e', 'i', 'o', 'u']:
                if c not in odd_vowels:
                    odd_vowels.add(c)
                else:
                    odd_vowels.remove(c)

        for i, c in enumerate(s):
            track_odd_vowels(odd_vowels, c)
            curr_odd_vowels = set([odd_vowel for odd_vowel in odd_vowels])
            for j in range(0, i + 1):
                if not curr_odd_vowels:
                    result = max(result, i - j + 1)
                track_odd_vowels(curr_odd_vowels, s[j])
        return result

"""
- prefix sum with hashmap
- O(n), O(n)
- intuition: in the previous solution we use odd_vowels to store current state, a substring s[a:b] will actually satisfy the condition when 
    its s[:a + 1] and s[:b + 1] have the same state. if we can seralize that state (using bit manipulation) and store the first occurrence of 
    each unique state, then we can find the subarray easily.
    
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        result = 0
        n = 0
        states = {0: -1}
        for i, c in enumerate(s):
            if c in vowels:
                n ^= vowels[c]
            if n not in states:
                states[n] = i
            else:
                result = max(result, i - states[n])
        return result
                
            
                
        
        