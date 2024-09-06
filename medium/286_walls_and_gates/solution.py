from typing import List
from collections import deque

class Solution:
    """
    DFS solution from each room
    Time complexity: O(mn^2)
    TLE on leetcode
    """
    def dfs(self, r, c, step):
        """
        r: row index
        c: col index
        step: step number
        """
        if (r < 0 or c < 0 or # out of bound of the room
            r >= self.ROWS or c >= self.COLS or # out of bound of the room
            self.rooms[r][c] == -1 or # meet a wall
            (r, c) in self.path): # already visited
            return
        if self.rooms[r][c] == 0: # meet a gate
            self.tmp_result = min(step, self.tmp_result)
            return
        
        step += 1
        self.path.add((r, c))
        self.dfs(r + 1, c, step)
        self.dfs(r - 1, c, step)
        self.dfs(r, c + 1, step)
        self.dfs(r, c - 1, step)
        self.path.remove((r, c))

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.ROWS = len(rooms)
        self.COLS = len(rooms[0])
        self.rooms = rooms
        self.result = rooms.copy()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.rooms[r][c] == 0 or self.rooms[r][c] == -1:
                    self.result.append(self.rooms[r][c])
                    continue
                self.tmp_result = float("inf")
                self.path = set()
                self.dfs(r, c, 0)
                if self.tmp_result < float("inf"):
                    self.result[r][c] = self.tmp_result

        return self.result
    
class NeetSolution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        BFS solution from each gate AT THE SAME TIME
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        def addRoom(r,c):
            """
            add room to the queue
            """
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visited or rooms[r][c] == -1):
                return
            visited.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visited.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)): # each level represents +1 distance from the gate
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1 # after we are done with the current level, we move to the next level