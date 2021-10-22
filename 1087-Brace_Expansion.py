"""
- string parsing
"""
class Solution:
    def expand(self, s: str) -> List[str]:
        result = ['']
        current = []
        has_multiple = False
        for c in s:
            if c == ',':
                continue
            elif c == "{":
                has_multiple = True
            elif c == "}":
                has_multiple = False
                result = [s + c for s in result for c in current]
                current.clear()
            else: # char
                if has_multiple:
                    bisect.insort(current, c)
                else:
                    result = [s + c for s in result]
        return result