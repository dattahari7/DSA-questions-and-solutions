# Implementing Dijkstra Algorithm

# Optimal Solution (using prority queue)

import heapq

def dijkstra(graph, start):
    # Number of nodes in the graph
    n = len(graph)
    
    # Distance array
    dist = [float('inf')] * n
    dist[start] = 0
    
    # Priority queue to store (distance, node)
    pq = [(0, start)]
    
    while pq:
        # Extract the node with the minimum distance
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip processing if we found a shorter path already
        if current_distance > dist[current_node]:
            continue
        
        # Process each neighbor of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path is found
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist


# Time Complexity: O((V + E)log(v)) Where E = Number of edges and V = Number of Nodes.
# Space Complexity: O(E + V) Where E = Number of edges and V = Number of Nodes.

# Optimal solution (using set)

class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        # Initialize distance array with infinity
        dist = [float('inf')] * V
        dist[S] = 0
        
        # Set to store the (distance, node) tuples
        st = set([(0, S)])
        
        while st:
            # Extract the node with the minimum distance
            curr_dist, curr_node = min(st)
            st.remove((curr_dist, curr_node))
            
            # Process each neighbor of the current node
            for adj_node, edgW in adj[curr_node]:
                new_dist = curr_dist + edgW
                
                # If a shorter path is found
                if new_dist < dist[adj_node]:
                    
                    # Remove the old distance if it's not infinity
                    if dist[adj_node] != float('inf'):
                        st.remove((dist[adj_node], adj_node))
                        
                    # Update the distance and add the new (distance, node) tuple
                    dist[adj_node] = new_dist
                    st.add((dist[adj_node], adj_node))
                    
        return dist

# Time Complexity: O((V + E)log(v)) Where E = Number of edges and V = Number of Nodes.
# Space Complexity: O(E + V) Where E = Number of edges and V = Number of Nodes.
