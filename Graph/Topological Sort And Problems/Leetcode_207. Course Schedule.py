# 207. Course Schedule

# Optimal Solution (using Topological Sort)

from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list for the graph
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)  # Course b is a prerequisite for course a

        # Initialize in-degree array to count prerequisites for each course
        indegree = [0] * numCourses
        for i in range(numCourses):
            for course in adj[i]:
                indegree[course] += 1  # Increase in-degree for each course dependent on i

        # Initialize queue with all courses having in-degree 0
        que = deque()
        for course in range(numCourses):
            if indegree[course] == 0:  # Courses with no prerequisites
                que.append(course)

        count = 0  # Counter for the number of courses that can be finished
        while que:
            course = que.popleft()  # Take course from the queue
            count += 1  # Increment the count of courses that can be finished
            # Reduce in-degree for all adjacent courses
            for rel_course in adj[course]:
                indegree[rel_course] -= 1  # One less prerequisite for rel_course
                # If in-degree becomes 0, add it to the queue
                if indegree[rel_course] == 0:
                    que.append(rel_course)
        
        # If count of finished courses equals the total number of courses, return True
        if numCourses == count:
            return True
        else:
            return False


# Time Complexity: O(V + E)
# Space Complexity: O(N)