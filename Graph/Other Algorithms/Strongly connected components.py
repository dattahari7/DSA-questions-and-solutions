# Strongly Connected Components

# Optimal Solution (using Kosaraju's Algorithm)

from collections import deque, defaultdict

class Solution:
    
    def dfs(self, node, vis, adj, stack):
        """
        Perform DFS to fill the stack with vertices in the order of their finishing times.

        Args:
        node (int): The current node to be visited.
        vis (List[bool]): List to track visited nodes.
        adj (List[List[int]]): Adjacency list of the graph.
        stack (deque): Stack to store the vertices in the order of their finishing times.
        """
        vis[node] = True
        
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it, vis, adj, stack)
        stack.append(node)

    def dfs3(self, node, vis, adjT):
        """
        Perform DFS on the transposed graph to find and mark all nodes in the current SCC.

        Args:
        node (int): The current node to be visited.
        vis (List[bool]): List to track visited nodes.
        adjT (defaultdict[list]): Adjacency list of the transposed graph.
        """
        vis[node] = True
        for it in adjT[node]:
            if not vis[it]:
                self.dfs3(it, vis, adjT)
    
    def kosaraju(self, V, adj):
        """
        Function to find the number of strongly connected components in the graph using Kosaraju's algorithm.

        Args:
        V (int): Number of vertices in the graph.
        adj (List[List[int]]): Adjacency list of the graph.

        Returns:
        int: Number of strongly connected components.
        """
        # Step 1: Perform a DFS and fill the stack with vertices in the order of their finishing times
        vis = [False] * V
        stack = deque()

        for i in range(V):
            if not vis[i]:
                self.dfs(i, vis, adj, stack)

        # Step 2: Transpose the graph
        adjT = defaultdict(list)
        for i in range(V):
            vis[i] = False  # Reset the visited array for the second pass
            for it in adj[i]:
                adjT[it].append(i)

        # Step 3: Perform DFS on the transposed graph in the order defined by the stack
        scc = 0
        while stack:
            node = stack.pop()
            if not vis[node]:
                scc += 1
                self.dfs3(node, vis, adjT)
                
        return scc


# Time Complexity: O(V+E) + O(V+E) + O(V+E) ~ O(V+E) , where V = no. of vertices, E = no. of edges. The first step is a simple DFS, so the first term is O(V+E). The second step of reversing the graph and the third step, containing DFS again, will take O(V+E) each.

# Space Complexity: O(V)+O(V)+O(V+E), where V = no. of vertices, E = no. of edges. Two O(V) for the visited array and the stack we have used. O(V+E) space for the reversed adjacent list.