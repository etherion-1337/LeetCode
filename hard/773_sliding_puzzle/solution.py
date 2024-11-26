from collections import deque
from typing import List

class Solution:
    """
    BFS solution

    BFS on board states. We start with the initial board state and keep track of the current index of 0.
    """
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # possible moves for each index
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        # flatten board
        b_flat = [c for row in board for c in row]
        # curr index (i.e. index of 0), board state, step length
        q = deque([(b_flat.index(0), b_flat, 0)])
        visited = set()

        while q:
            i, b, length = q.popleft()

            if b == [1, 2, 3, 4, 5, 0]:
                return length

            for j in adj[i]:
                new_b = b.copy()
                new_b[i], new_b[j] = b[j], b[i]
                new_b_str = "".join([str(c) for c in new_b])
                if new_b_str not in visited:
                    q.append((j, new_b, length + 1))
                    visited.add(new_b_str)

        return -1