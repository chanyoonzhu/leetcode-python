"""
- string
- O(n), O(n)
"""
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        words = sentence.split(" ")
        
        for i, word in enumerate(words):
            translated = word if word[0] in vowels else word[1:] + word[0]
            translated += ("ma" + "a" * (i + 1))
            words[i] = translated
        
        return ' '.join(words)