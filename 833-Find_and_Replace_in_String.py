class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        
        S = list(S)
        
        for i, source, target in sorted(zip(indexes, sources, targets), reverse = True):
            
            if all(i+j < len(S) and source[j] == S[i+j] for j in range(len(source))):
                S[i:i+len(source)] = list(target)
                
        return "".join(S)