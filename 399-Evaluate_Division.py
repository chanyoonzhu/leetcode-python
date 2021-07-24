"""
- graph bfs search
- O(n*E), O(E) n - number of queries E - number of equations
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            graph[x][y] = value
            graph[y][x] = 1.0 / value
        
        visited = set()
        result = []
        for query in queries:
            found = False
            src, dest = query
            q = [(src, 1)]
            visited.add(src)
            while q:
                v, div = q.pop(0)
                if v == dest and v in graph: # v in graph check: easy to miss for [x:x] x not in equation case
                    result.append(div)
                    found = True
                else:
                    for neib, neib_div in graph[v].items():
                        if neib not in visited:
                            visited.add(neib)
                            q.append((neib, div * neib_div))
            if not found: result.append(-1.0)
            q.clear()
            visited.clear()
        return result

"""
- union find
- O((n+E)*logE), O(E) n - number of queries E - number of equations
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parents = {}
	
        def find(v):
            p, vratio = parents.setdefault(v, (v, 1.0))
            if v != p:
                pp, pratio = find(p)
                parents[v] = (pp, vratio * pratio)
            return parents[v]

        def union(x, y, ratio):
            xparent, xratio, yparent, yratio = *find(x), *find(y)
            if xparent != yparent:
                parents[xparent] = (yparent, yratio / xratio * ratio)

        for (x, y), v in zip(equations, values):
            union(x, y, v)
        
        result = []
        for x, y in queries:
            if x not in parents or y not in parents:
                ratio = -1
            else:
                xparent, xratio, yparent, yratio = *find(x), *find(y)
                ratio = xratio / yratio if xparent == yparent else -1.0
            result.append(ratio)
        return result