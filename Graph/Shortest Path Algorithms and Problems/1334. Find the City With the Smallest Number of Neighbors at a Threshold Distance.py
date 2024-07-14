# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

# Optimal Solution (using floyd warshall algorithm)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize distance matrix with infinity (inf)
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Set initial distances based on given edges
        for u, v, w in edges:
            dist[u][v] = w  # Distance from u to v
            dist[v][u] = w  # Distance from v to u (since it's an undirected graph)

        # Distance from a city to itself is 0
        for i in range(n):
            dist[i][i] = 0

        # Floyd-Warshall algorithm to find the shortest paths between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # If there is no path through k, continue
                    if dist[i][k] == float('inf') or dist[k][j] == float('inf'):
                        continue
                    # Update the distance from i to j through k
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Initialize variables to track the city with the smallest number of reachable cities
        cntCity = n  # Maximum possible count
        cityNo = -1  # City with the smallest number of reachable cities

        # Iterate through each city to count the number of reachable cities within the distance threshold
        for city in range(n):
            cnt = 0
            for adjcity in range(n):
                if dist[city][adjcity] <= distanceThreshold:
                    cnt += 1
            # Update the city if it has fewer or equal reachable cities within the threshold
            if cnt <= cntCity:
                cntCity = cnt
                cityNo = city
        
        # Return the city with the smallest number of reachable cities within the distance threshold
        return cityNo


# Time Complexity: O(V3), as we have three nested loops each running for V times, where V = no. of vertices.

# Space Complexity: O(V2), where V = no. of vertices. This space complexity is due to storing the adjacency matrix of the given graph.


# Optimal Solution (using Dijkstra's algorithm)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create adjacency list from the edges
        adjList = defaultdict(list)
        for u, v, w in edges:
            adjList[u].append((v, w))  # Add edge from u to v with weight w
            adjList[v].append((u, w))  # Add edge from v to u with weight w (since it's undirected)
            
        cityNo = cntCity = float('inf')  # Initialize city number and count of reachable cities
        for city in range(n):
            # Initialize distances with infinity and set the distance to the starting city as 0
            dist = [float('inf')] * n
            dist[city] = 0
            pq = [(0, city)]  # Priority queue for Dijkstra's algorithm
            
            # Dijkstra's algorithm to find the shortest paths from the city
            while pq:
                wth, node = heapq.heappop(pq)

                for adj_node, ewth in adjList[node]:
                    # If a shorter path to adj_node is found, update the distance and push it to the priority queue
                    if wth + ewth < dist[adj_node]:
                        dist[adj_node] = wth + ewth
                        heapq.heappush(pq, (dist[adj_node], adj_node))
            
            # Count the number of cities reachable within the distance threshold
            count = 0
            for adjCity in range(n):
                if dist[adjCity] <= distanceThreshold:
                    count += 1
            
            # Update the city with the smallest number of reachable cities within the threshold
            if count <= cntCity:
                cntCity = count
                cityNo = city
        
        # Return the city with the smallest number of reachable cities within the distance threshold
        return cityNo

