# 787. Cheapest Flights Within K Stops

# Optimal Solution (only using queue)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create an adjacency list for the graph
        adj_list = [[] for _ in range(n)]
        for u, v, price in flights:
            adj_list[u].append((v, price))

        # Initialize distance array with infinity
        dist = [float('inf')] * n
        # Use a deque as a queue to perform BFS
        que = deque([(0, src, 0)])  # (current stop, current node, current price)
        dist[src] = 0

        while que:
            # Pop the leftmost element in the queue
            curr_stop, curr_node, curr_price = que.popleft()
            # Skip if the number of stops exceeds k
            if curr_stop > k:
                continue

            # Explore all adjacent nodes
            for adj_node, cost in adj_list[curr_node]:
                # Calculate new price to reach the adjacent node
                new_price = cost + curr_price
                # Update the distance if a cheaper price is found
                if new_price < dist[adj_node] and curr_stop <= k:
                    dist[adj_node] = new_price
                    que.append((curr_stop + 1, adj_node, new_price))

        # Return -1 if the destination is not reachable
        if dist[dst] == float('inf'):
            return -1
        # Return the minimum price to reach the destination
        return dist[dst]

# Time Complexity: O( N ) { Additional log(N) of time eliminated here because we’re using a simple queue rather than a priority queue which is usually used in Dijkstra’s Algorithm }.
# Space Complexity: O( |E| + |V| ) { for the adjacency list, queue, and the dist array }.
