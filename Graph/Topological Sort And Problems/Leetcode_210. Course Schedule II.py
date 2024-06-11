# 210. Course Schedule II

# Optimal Solution (using Topological Sort)

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list for the graph
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Populate the graph and in-degree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # Add edge from prereq to course
            indegree[course] += 1  # Increase in-degree for course

        # Initialize a queue with all courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []  # List to store the order of courses

        while queue:
            course = queue.popleft()  # Take course from the queue
            order.append(course)  # Append course to the order
            for next_course in graph[course]:  # Iterate over dependent courses
                indegree[next_course] -= 1  # Decrease in-degree for next_course
                if indegree[next_course] == 0:  # If in-degree becomes 0, add to queue
                    queue.append(next_course)

        # Check if topological sort is possible
        if len(order) == numCourses:
            return order  # Return the order of courses
        else:
            return []  # Return an empty list if not all courses can be taken


# Time Complexity: O(V + E)
# Space Complexity: O(N)