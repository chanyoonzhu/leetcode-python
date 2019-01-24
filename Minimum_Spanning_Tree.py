"""
629. Minimum Spanning Tree
Difficulty: Hard

http://www.lintcode.com/en/problem/minimum-spanning-tree/

Given a list of Connections, which is the Connection class (the city name at both ends of the edge and a cost between them), find some edges, connect all the cities and spend the least amount. Return the connects if can connect all the cities, otherwise return empty list.

Notice

Return the connections sorted by the cost, or sorted city1 name if their cost is same, or sorted city2 if their city1 name is also same.

Example
Gievn the connections = ["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]

Return ["Acity","Bcity",1], ["Acity","Ccity",2]
"""

def Prim(connections):

    def findMin(arr):
        min, idx = float('inf'), 0
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
                idx = i
        return (idx, min)
    
    def findIndex(element, arr):
        for i in range(len(arr)):
            if arr[i] == element:
                return i
        return -1
    
    def updateNeighbors(node_idx):
        node = nodes[node_idx]
        for connection in connections:
            neighbor = ""
            if connection[0] == node:
                neighbor = connection[1]
            elif connection[1] == node:
                neighbor = connection[0]
            neighbor_idx = findIndex(neighbor, nodes)
            if neighbor_idx != -1 and distance[neighbor_idx] > connection[2]:
                distance[neighbor_idx] = connection[2]
                parents[neighbor_idx] = node
                

    if not connections:
        return []
    
    span = []
    nodes = list(set([connection[0] for connection in connections]).union(set([connection[1] for connection in connections])))
    
    distance = [float('inf')] * len(nodes)
    parents = [None] * len(nodes)
    
    distance[0] = 0
    
    while nodes:
        # find node with min distance
        min = findMin(distance)
        min_node_idx = min[0]
        min_distance = min[1]
        # if there's nodes not connected, return []
        if min_distance == float('inf'):
            return []
        # add edge to its parent to result
        if parents[min_node_idx]:
            span.append([parents[min_node_idx], nodes[min_node_idx], min_distance])
        # update its neighbor's distance
        updateNeighbors(min_node_idx)
        # remove node from list
        del nodes[min_node_idx]
        del distance[min_node_idx]
        del parents[min_node_idx]

    return span

def Kruskal(connections):

    res = []
    parent, rank = [], []
    connections = sorted(sorted(sorted(connections,key=lambda x: x[0]),key=lambda x: x[1]),key=lambda x: x[2])

    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])
    
    def union(parent, rank, x, y):
        xParent = find(parent, x)
        yParent = find(parent, y)

        if rank[xParent] < rank[yParent]:
            parent[xParent] = yParent
        elif rank[xParent] > rank[yParent]:
            parent[yParent] = xParent
        else:
            parent[yParent] = xParent 
            rank[xParent] += 1

    totalN, dic = 0, {}
    for connection in connections:
        if connection[0] not in dic:
            dic[connection[0]] = totalN
            parent.append(totalN)
            rank.append(0)
            totalN += 1
        if connection[1] not in dic:
            dic[connection[1]] = totalN
            parent.append(totalN)
            rank.append(0)
            totalN += 1
    
    for connection in connections:
        head, tail, k = connection
        headParent = find(parent, dic[head])
        tailParent = find(parent, dic[tail])

        if headParent != tailParent:
            res.append([head, tail, k])
            union(parent, rank, headParent, tailParent)
    
    if len(res) == totalN - 1:
        return res
    else:
        []

graph = [["Acity","Ccity",2], ["Acity","Bcity",2], ["Bcity","Ccity",1]]
# print(Prim(graph))
print(Kruskal(graph))        
        
        
        
    
    
    