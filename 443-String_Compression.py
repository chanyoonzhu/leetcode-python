"""
- string
- O(n), O(1)
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        chars.append("\v") # dummy value
        prev, count = chars[0], 0
        i = 0
        for c in chars:
            if c == prev:
                count += 1
            else:
                chars[i] = prev
                i += 1
                if count != 1:
                    for cc in str(count):
                        chars[i] = cc
                        i += 1
                count = 1
                prev = c

        return i