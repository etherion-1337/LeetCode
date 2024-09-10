from typing import List

class Solution:
    def dfs(self, course):
        # within one dfs run, if revisit means cyclic
        if course in self.visited:
            return False
        # if this node has been cleared and it is a good node
        if self.pre_req_map[course] == []:
            return True

        # current dfs path visited add
        self.visited.add(course)
        # for each pre_req, we run dfs to check its subsequent pre req
        for pre_req in self.pre_req_map[course]:
            _tmp_result = self.dfs(pre_req)
            if not _tmp_result:
                return False
        # if this node is good we remove from current dfs
        self.visited.remove(course)
        # and if all pre req is good we clear this node
        self.pre_req_map[course] = []
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # hashmap to store adjancy list
        # {course: [pre_req courses]}
        self.pre_req_map = {i:[] for i in range(numCourses)}
        # visisted path for the current dfs
        self.visited = set()
        
        # populate the adjancy list
        for course, pre_req in prerequisites:
            self.pre_req_map[course].append(pre_req)

        # for each course we run dfs because part of the graph can be disconnected
        for course in range(numCourses):
            result = self.dfs(course)
            if not result:
                return False
        
        return True
        
class NeetSolution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
