"""
- 第一问是只有0个parents和只有1个parent的节点
"""
print("Hello, world!")
print("This is a fully functioning Python 3 environment.")

# Your previous work is preserved below:
#
# * Hello, world!
# * This is a fully functional Markdown environment.
#
import collections

def getNodesWithZeroOrOneParent(connections: list) -> list:
    graph = collections.defaultdict(set)
    for parent, child in connections:
        graph[child].add(parent)
        graph[parent] = set()
        
    res = []
    for key, val in graph.items():
        if len(val) == 0 or len(val) == 1:
            res.append(key)
    return res

# {{1,4}, {1,5}, {2,5}, {3,6}, {6,7}}
print(getNodesWithZeroOrOneParent([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]))

def hasCommonAncestor(edges, x, y):
    graph = collections.defaultdict(set)
    for parent, child in edges:
        graph[child].add(parent)
        
    x_parents = set([x])
    q = [x]
    while q:
        node = q.pop(0)
        for parent in graph[node]:
            x_parents.add(parent)
            q.append(parent)
        
    q = [y]
    while q:
        node = q.pop(0)
        if node in x_parents:
            return True
        for parent in graph[node]:
            q.append(parent)
    return False

print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 4, 5))
print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 4, 1))
print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 5, 1))
print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 6, 7))
print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 4, 3))
print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 5, 3))
print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 1, 3))

def findFarthestAncestor(edges, x, y):
    graph = collections.defaultdict(set)
    for parent, child in edges:
        graph[child].add(parent)
        
    x_parents = dict()
    q = [(x, 0)]
    while q:
        node, height = q.pop(0)
        for parent in graph[node]:
            x_parents[parent] = height + 1
            q.append((parent, height + 1))
        
    q = [y]
    res = (None, 0) # node, height
    while q:
        node = q.pop(0)
        if node in x_parents and x_parents[node] > res[1]:
            res = (node, x_parents[node])
        for parent in graph[node]:
            q.append(parent)
    return res[0]

print(findFarthestAncestor([[1, 2], [2,4], [1,3], [3, 4],[3,5]], 4, 5))
# print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 4, 1))
# print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 5, 1))
# print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 6, 7))
# print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 4, 3))
# print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 5, 3))
# print(hasCommonAncestor([[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]], 1, 3))