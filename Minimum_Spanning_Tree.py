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

graph = [["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]]
print(Prim(graph))
        
        
        
        
    
    
    