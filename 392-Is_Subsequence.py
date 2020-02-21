class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sIdx, tIdx, sLen, tLen = 0, 0, len(s), len(t)
        
        while sIdx < sLen and tIdx < tLen:
            if s[sIdx] == t[tIdx]:
                sIdx += 1
            tIdx += 1
        return True if sIdx == sLen else False
                
            
        