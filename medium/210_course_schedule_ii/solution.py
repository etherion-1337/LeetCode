from typing import List

class Solution:
    """
    DFS solution
    similar to 207_course_schedule
    
    This is actually topological sort
    Time complexity: O(V+E)
    """
    def dfs(self, course):
        if course in self.cycle:
            return False
        if course in self.visited:
            return True

        self.cycle.add(course)
        for pre_req in self.pre_req_map[course]:
            _tmp_result = self.dfs(pre_req)
            if not _tmp_result:
                return False
        self.cycle.remove(course)
        self.visited.add(course)
        self.result.append(course)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the adjacency list of pre_req
        self.pre_req_map = {i:[] for i in range(numCourses)}
        self.cycle = set()
        self.visited = set()
        self.result = []
        for course, pre_req in prerequisites:
            self.pre_req_map[course].append(pre_req)

        for course in range(numCourses):
            res = self.dfs(course)
            if not res:
                return []
        
        return self.result
    
class NeetSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
