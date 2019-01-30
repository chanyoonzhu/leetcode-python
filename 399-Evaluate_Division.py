class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        dic, idxes = {}, {}
        idx = 0
        res = []
        
        for i in range(len(equations)):
            if equations[i][0] in dic:
                dic[equations[i][0]].append((equations[i][1], values[i]))
            else:
                dic[equations[i][0]] = [(equations[i][1], values[i])]
                idxes[equations[i][0]] = idx
                idx += 1
            if equations[i][1] in dic:
                dic[equations[i][1]].append((equations[i][0], 1 / values[i]))
            else:
                dic[equations[i][1]] = [(equations[i][0], 1 / values[i])]
                idxes[equations[i][1]] = idx
                idx += 1
        
        for query in queries:
            
            if query[0] not in idxes or query[1] not in idxes:
                res.append(-1.0)
                continue
                
            visited = [0] * (idx + 1)
            q = [(query[0], 1.0)]
            visited[idxes[query[0]]] = 1
            ans = -1
            while q:
                curr = q[0]
                del q[0]
                if curr[0] == query[1]:
                    ans = curr[1]
                    res.append(ans)
                else:
                    neighbors = dic[curr[0]]
                    for nb in neighbors:
                        if not visited[idxes[nb[0]]]:
                            visited[idxes[nb[0]]] = 1
                            if nb[0] == query[1]:
                                ans = curr[1] * nb[1]
                                res.append(ans)
                            else:
                                q.append((nb[0], curr[1] * nb[1]))
            if ans < 0:
                res.append(-1.0)
                
        return res
    
sl = Solution()
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
# print(equations[0][0])
print(sl.calcEquation(equations, values, queries))
            