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

    def updateSets(sets, nodeA, nodeB):
        setA_idx = setB_idx = -1
        for i in range(len(sets)):
            if nodeA in sets[i]:
                setA_idx = i
            if nodeB in sets[i]:
                setB_idx = i
        if setA_idx != -1 and setB_idx != -1: # both are connected to other separate node groups
            sets[setA_idx].union(sets[setB_idx])
        elif setA_idx == -1 and setB_idx != -1: # B is connected, A is not
            sets[setB_idx].add(nodeA)
        elif setA_idx != -1 and setB_idx == -1: # A is connected, B is not
            sets[setA_idx].add(nodeB)
        else: # neither A or B is connected
            sets.append(set([nodeA, nodeB])) 

    span = []
    sets = []

    edge_sort = sorted(connections,key=lambda x: x[2])
    # add edge with min weight to spanning tree
    for e in edge_sort:
        # check if nodes at the end of edge belong to the same set (already connected)
        connected = False
        for s in sets:
            if e[0] in s and e[1] in s:
                connected = True
                break
        if not connected:
            span.append(e)
            # update sets
            updateSets(sets, e[0], e[1])
    # test if all nodes are connected
    if len(sets) > 1:
        return []

    return span

graph = [["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]]
# print(Prim(graph))
print(Kruskal(graph))        
        
        
        
    
    
    