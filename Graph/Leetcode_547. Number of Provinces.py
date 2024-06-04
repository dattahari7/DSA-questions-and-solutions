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
                
