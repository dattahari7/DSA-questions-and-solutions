# Alien Dictionary

# Optimal Solution (using Kahn's Algorithm)

from collections import deque, defaultdict

class Solution:
    def topoSort(self, V, adj_list):
        indegree = [0] * V  # Initialize in-degree array for all vertices
        for i in range(V):
            for node in adj_list[i]:  # Update in-degrees based on edges
                indegree[node] += 1
        que = deque()  # Initialize queue for vertices with in-degree 0
        for i in range(V):
            if indegree[i] == 0:  # Enqueue vertices with in-degree 0
                que.append(i)
        
        topo = []  # List to store topological order
        while que:
            node = que.popleft()  # Dequeue a vertex with in-degree 0
            topo.append(node)
            for adj_node in adj_list[node]:  # For all adjacent vertices
                indegree[adj_node] -= 1  # Reduce in-degree by 1
                if indegree[adj_node] == 0:  # If in-degree becomes 0, enqueue it
                    que.append(adj_node)
        if len(topo) == V:  # Check if topological sort includes all vertices
            return topo  # Return topological order
        else:
            return []  # Return empty list if graph is not a DAG
                
    def findOrder(self, alien_dict, N, K):
        adj_list = defaultdict(list)  # Create adjacency list
        for i in range(N-1):
            s1 = alien_dict[i]  # Current word
            s2 = alien_dict[i+1]  # Next word
            min_len = min(len(s1), len(s2))  # Find the minimum length of the two words
            for ptr in range(min_len):
                if s1[ptr] != s2[ptr]:  # Find the first non-matching character
                    adj_list[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))  # Create a directed edge
                    break  # Only consider the first non-matching character
                
        topo = self.topoSort(K, adj_list)  # Get topological sort of the graph
        if not topo:
            return ""  # Return empty string if topological sort is not possible
        
        return "".join(chr(char + ord('a')) for char in topo)  # Convert topological order to characters


# Time Complexity: O(N * min_len) + O(K + E) here min_len is minimum lenght of word
# Space Complexity: O(K) here K is starting word