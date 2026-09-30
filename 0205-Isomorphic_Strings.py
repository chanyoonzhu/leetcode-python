class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dicS = collections.defaultdict(list)
        dicT = collections.defaultdict(list)
        
        for i, c in enumerate(s):
            dicS[c].append(i)
        
        for i, c in enumerate(t):
            dicT[c].append(i)
        
        return sorted(dicS.values()) == sorted(dicT.values())

        """
        - map
        """
        return map(s.find, s) == map(t.find, t)