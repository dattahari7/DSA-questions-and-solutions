# 743. Network Delay Time

# Optimal Solution (using Dijkstra's Algorithm)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Initialize the adjacency list
        adj = defaultdict(list)
        for u, v, w in times:  # u is the starting node, v is the ending node, w is the weight (time)
            adj[u].append((v, w))  # Add the edge to the adjacency list
        
        # Initialize the list to store the shortest times to each node
        shortest_times = [float('inf')] * n  # Set all times to infinity initially
        shortest_times[k - 1] = 0  # Starting node's time to itself is 0
        
        # Initialize the priority queue with the starting node
        pq = [(0, k)]  # (distance, node)
        
        while pq:
            current_time, u = heapq.heappop(pq)  # Get the node with the smallest current time
            # Iterate over adjacent nodes
            for v, travel_time in adj[u]:
                # If the time to node v through node u is shorter, update and push to the priority queue
                if shortest_times[v - 1] > current_time + travel_time:
                    shortest_times[v - 1] = current_time + travel_time
                    heapq.heappush(pq, (shortest_times[v - 1], v))
        
        # Get the maximum time from the shortest times to determine network delay
        max_time = max(shortest_times)
        
        return max_time if max_time != float('inf') else -1  # If there's an unreachable node, return -1


# Time complexity:
# O(n*logn)

# Space complexity:
# O(n)