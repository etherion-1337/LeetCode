from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Greedy algo
        time complexity: O(n)
        space complexity: O(1)
        
        from starting pos, track total gas currently the car has and reset once this total < 0
        we do not have to go through from the start (cyclic) again because
        1. there is guarantee a solution (after the first check) and it is unique
        2. once we find an (most left) idx that can sustain all the way to the end (right), then this idx must be able to sustain the entire loop
        because we want an idx that can stretch the longest possible, if we choose another (more right idx), then it is worse than the (more left) idx 
        """
        if sum(gas) - sum(cost) < 0:
            return -1

        start = 0
        total = 0

        for idx in range(len(gas)):
            total += gas[idx] - cost[idx]

            if total < 0:
                total = 0
                start = idx + 1

        return start