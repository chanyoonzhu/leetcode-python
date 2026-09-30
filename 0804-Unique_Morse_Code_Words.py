"""
- hashset
- O(nw), O(nw)
"""
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        transformations = set()
        for word in words:
            transformations.add(self.transform(word))
        
        return len(transformations)
    
    def transform(self, word):
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = ""
        for c in word:
            res += code[ord(c) - ord("a")]
        return res
        