class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        """
        - topological sort (bfs)
        """
        
        chars = set(''.join(words))
        afterDic = collections.defaultdict(set) 
        ins = [0] * 26 # number of in nodes of each character
        
        idx = 0
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):  # classic zip!
                if a != b:
                    if b not in afterDic[a]: # don't forget this or you will give b more ins value than actually is
                        afterDic[a].add(b)
                        ins[ord(b)-ord('a')] += 1
                    break
        
        q, res = [], ""
    
        for i in range(26):
            c = chr(ord('a')+i)
            if c in chars and ins[i] == 0:
                q.append(c)
        
        for _ in range(len(chars)):
            if not q:
                return "" # topological sort - exit when a char cannot be selected
            curr = q.pop(0)
            res += curr
            for prec in afterDic[curr]:
                ins[ord(prec)-ord('a')] -= 1
                if ins[ord(prec)-ord('a')] == 0:
                    q.append(prec)
        
        return res 

sl = Solution()
print(sl.alienOrder(["za","zb","ca","cb"]))