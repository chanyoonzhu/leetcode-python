import re

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper()
        S = re.sub('-', '', S)
        i = len(S) - K
        while i > 0:
            S = S[:i] + '-' + S[i:]
            i -= K
        
        return S