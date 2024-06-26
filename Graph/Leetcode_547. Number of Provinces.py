# 547. Number of Provinces

# BruteForce Solution (Converting adj matrix to adjList)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Number of vertices in the graph (number of cities)
        V = len(isConnected)
        
        # Create an adjacency list from the adjacency matrix
        adjList = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                # If there is a connection between city i and city j, add it to the adjacency list
                if isConnected[i][j] == 1 and i != j:
                    adjList[i].append(j)
                    adjList[j].append(i)
        
        # Visited array to keep track of visited cities
        vis = [0] * V
        
        # Initialize the count of connected components (provinces)
        count = 0

        # Iterate through each city
        for i in range(V):
            # If the city has not been visited, it's a new province
            if vis[i] == 0:
                count += 1
                # Perform a DFS to mark all cities in this province as visited
                self.dfs(i, vis, adjList)
        
        # Return the number of provinces
        return count

    def dfs(self, node, vis, adjList):
        # Mark the current city as visited
        vis[node] = 1
        
        # Visit all connected cities (adjacent vertices)
        for vertex in adjList[node]:
            if vis[vertex] == 0:
                self.dfs(vertex, vis, adjList)


# Time Complexity: O(N * N)
# Space Complexity: O(N) with extra space of adjList


# Optimal Solution

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Number of vertices (cities)
        V = len(isConnected)
        # Set to keep track of visited cities
        vis = set()
        # Initialize the count of provinces
        count = 0
        # Iterate through each city
        for i in range(V):
            # If the city has not been visited, it's a new province
            if i not in vis:
                count += 1
                # Perform a DFS to mark all cities in this province as visited
                self.dfs(i, vis, isConnected)
        # Return the number of provinces
        return count

    def dfs(self, node, vis, isConnected):
        # Mark the current city as visited
        vis.add(node)
        # Visit all connected cities (adjacent vertices)
        for i in range(len(isConnected)):
            if isConnected[node][i] and i not in vis:
                self.dfs(i, vis, isConnected)
   

# Time Complexity: O(N * N)
# Space Complexity: O(N) only recursive stack space
                
# Optimal Solution (using union find)

class DisjointSetUnion:
    def __init__(self, n):
        # Initialize parent array where each node is its own parent
        self.parent = list(range(n + 1))
        # Initialize sizes of each set to 1
        self.size = [1] * (n + 1)

    def find(self, u):
        # Find with path compression
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by size
        root_u = self.find(u)  # Find root of u
        root_v = self.find(v)  # Find root of v
        if root_u != root_v:
            # Attach smaller tree under root of larger tree
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DisjointSetUnion(n)
        
        # Union nodes if they are connected
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)

        # Count unique parents to determine the number of connected components
        count = 0
        for i in range(n):
            if dsu.parent[i] == i:
                count += 1

        return count


# Time Complexity: O(N * N)
# Space Complexity: O(N) only recursive stack space