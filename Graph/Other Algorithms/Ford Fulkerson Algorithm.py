# Ford Fulkerson Algorithm


def ford_fulkerson(graph, source, sink):
    max_flow = 0
    parent = [-1] * len(graph)
    
    while bfs(graph, source, sink, parent):
        # Find the maximum flow through the path found.
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        
        # update residual capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = []
    queue.append(source)
    visited[source] = True
    
    while queue:
        u = queue.pop(0)
        
        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                
                if ind == sink:
                    return True
    
    return False
