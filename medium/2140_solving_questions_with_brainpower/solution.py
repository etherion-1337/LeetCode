from typing import List

class Solution:
    """
    Brute force solution using backtracking.
    Time complexity: O(2^n)
    Space complexity: O(n) for recursion stack.
    """
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        def backtrack(i):
            if i >= len(questions):
                return 0

            points, brainpower = questions[i]

            return max(
                backtrack(i + 1), # skip
                points + backtrack(i + 1 + brainpower) # do qn
            )

        return backtrack(0)
    

class Solution:
    """
    memoization solution using backtracking.
    Also this is top-down dynamic programming.
    Time complexity: O(n)
    Space complexity: O(n) for recursion stack and memoization cache.
    """
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = [0] * len(questions)

        def backtrack(i):
            if i >= len(questions):
                return 0
            if cache[i]:
                return cache[i]

            points, brainpower = questions[i]

            cache[i] = max(
                backtrack(i + 1), # skip
                points + backtrack(i + 1 + brainpower) # do qn
            )
            return cache[i]

        return backtrack(0)
    

class Solution:
    """
    bottom-up dynamic programming solution.
    Time complexity: O(n)
    Space complexity: O(n) for cache.
    """
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        cache = [0] * N

        for i in reversed(range(N)):
            points, brainpower = questions[i]
            next_idx = i + 1 + brainpower

            skip = cache[i + 1] if i + 1 < N else 0
            choose = points + (cache[next_idx] if next_idx < N else 0)

            cache[i] = max(skip, choose)

        return cache[0]
    

