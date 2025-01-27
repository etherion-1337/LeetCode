from collections import defaultdict
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, course in prerequisites:
            adj[course].append(prereq)

        def dfs(course):
            if course not in prereq_map:
                prereq_map[course] = set()
                for prereq in adj[course]:
                    prereq_map[course] |= dfs(prereq) # union
                prereq_map[course].add(course)
            return prereq_map[course]

        prereq_map = {} # map course -> set of indirect pre req
        for course in range(numCourses):
            dfs(course)

        ans = []
        for u, v in queries:
            ans.append(u in prereq_map[v])

        return ans