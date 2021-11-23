"""
- merge interval
"""
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        N = len(s)
        # a list of booleans for each character in s
        bolds = [False] * N
        res = []
        
        # mark words to be bolded as True.
        for word in words:
            word_len = len(word)
            start = s.find(word)
            while start != -1:
                for k in range(start, start + word_len):
                    bolds[k] = True
                start = s.find(word, start + 1)
        
        prev_is_bold = False
        for i, is_bold in enumerate(bolds):
            if is_bold and not prev_is_bold:
                res.append("<b>")
                res.append(s[i])
            elif not is_bold and prev_is_bold:
                res.append("</b>")
                res.append(s[i])
            else:
                res.append(s[i])
            prev_is_bold = is_bold
        if prev_is_bold: res.append("</b>")
        
        return ''.join(res)

"""
- todo: Trie + merge interval
"""