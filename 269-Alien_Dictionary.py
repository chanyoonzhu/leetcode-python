"""
- topological sort with bfs
- key: compare words pair by pair
"""      
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        chars = set(''.join(words))
        afterDic = collections.defaultdict(set) 
        indegrees = [0] * 26 
        
        for pair in zip(words, words[1:]): # for each iteration, compare word to its next word
            for a, b in zip(*pair):
                if a != b:
                    if b not in afterDic[a]: # easy to miss: dedup
                        afterDic[a].add(b)
                        indegrees[ord(b) - ord('a')] += 1
                    break # easy to miss: only handles the first a != b
        
        q, res = [], ""
    
        q = [chr(ord('a') + i) for i, d in enumerate(indegrees) if d == 0 and chr(ord('a') + i) in chars]
        
        while q:
            curr = q.pop(0)
            res += curr
            for nextt in afterDic[curr]:
                indegrees[ord(nextt)-ord('a')] -= 1
                if indegrees[ord(nextt)-ord('a')] == 0:
                    q.append(nextt)
        
        return res 

sl = Solution()
print(sl.alienOrder(["za","zb","ca","cb"]))