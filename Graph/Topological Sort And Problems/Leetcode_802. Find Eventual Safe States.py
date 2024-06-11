# 802. Find Eventual Safe States

# Optimal Solution (Using Kahn's algorithm)

from collections import defaultdict, deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)  # Number of nodes in the graph
        adjRev = defaultdict(list)  # To store the reversed graph
        indegree = [0] * N  # To store the in-degrees of nodes

        # Build the reversed graph and compute in-degrees
        for i in range(N):
            for node in graph[i]:
                adjRev[node].append(i)  # Add edge in the reversed graph
                indegree[i] += 1  # Increase the in-degree of node i

        que = deque()  # Initialize a queue for nodes with 0 in-degree
        for i in range(N):
            if indegree[i] == 0:  # If the node has 0 in-degree, add it to the queue
                que.append(i)
        
        safeNodes = []  # List to store safe nodes
        while que:
            node = que.popleft()  # Process nodes with 0 in-degree
            safeNodes.append(node)
            # Decrease the in-degree of adjacent nodes in the reversed graph
            for adj_node in adjRev[node]:
                indegree[adj_node] -= 1  # Decrease in-degree by 1
                # If in-degree becomes 0, add to the queue
                if indegree[adj_node] == 0:
                    que.append(adj_node)
        
        safeNodes.sort()  # Sort the safe nodes in ascending order
        return safeNodes  # Return the list of safe nodes


# Time Complexity: O(V + E) + O(nlog(n))
# Space Complexity: O(N)