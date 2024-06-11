# 785. Is Graph Bipartite?

# Optimal Solution (using BFS)

class Solution:
    def bfs(self, start, color, graph):
        # Initialize the queue with the starting node
        que = deque([start])
        # Assign the starting node with color 0
        color[start] = 0
        
        while que:
            # Pop the front node from the queue
            node = que.popleft()
            # Traverse all adjacent nodes
            for adj_node in graph[node]:
                # If the adjacent node is not colored, color it with the alternate color
                if color[adj_node] == -1:
                    color[adj_node] = 1 - color[node]
                    # Add the adjacent node to the queue
                    que.append(adj_node)
                # If the adjacent node has the same color, the graph is not bipartite
                elif color[adj_node] == color[node]:
                    return False
        # If no conflicts were found, return True
        return True
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Initialize the color array with -1, indicating no color assigned yet
        color = [-1] * len(graph)
        # Check each node in the graph
        for i in range(len(graph)):
            # If the node is not colored, perform BFS to check bipartiteness
            if color[i] == -1:
                if self.bfs(i, color, graph) == False:
                    return False
        # If no conflicts were found, the graph is bipartite
        return True



# Time Complexity: O(V + 2E)
# Space Complexity: O(V)
    


# Optimal Solution (using DFS)

class Solution:
    def dfs(self, node, col, color, graph):
        # Assign the current node with the given color
        color[node] = col
        # Traverse all adjacent nodes
        for adj_node in graph[node]:
            # If the adjacent node is not colored, recursively color it with the alternate color
            if color[adj_node] == -1:
                if self.dfs(adj_node, 1 - col, color, graph) == False:
                    return False
            # If the adjacent node has the same color, the graph is not bipartite
            elif color[adj_node] == col:
                return False
        # If no conflicts were found, return True
        return True
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Initialize the color array with -1, indicating no color assigned yet
        color = [-1] * len(graph)
        # Check each node in the graph
        for i in range(len(graph)):
            # If the node is not colored, perform DFS to check bipartiteness
            if color[i] == -1:
                if self.dfs(i, 0, color, graph) == False:
                    return False
        # If no conflicts were found, the graph is bipartite
        return True


# Time Complexity: O(V + 2E)
# Space Complexity: O(V)