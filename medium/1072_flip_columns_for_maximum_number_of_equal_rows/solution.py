from typing import List
import collections

class Solution:
    """
    time complexity: O(n*m)
    space complexity: O(n)

    we observe that 2 rows are equal if they have the same pattern: either they are the same or they are the opposite
    if opposite we can col flip so that each row are consistent
    """
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # key: row pattern 
        # (0, 0, 1) and (1, 1, 0) counted as same and will store the one with tuple[0] is 0
        # val: freq
        row_type = {}

        for row in matrix:
            if row[0] == 1:
                tmp = [0 if n == 1 else 1 for n in row]
            else:
                tmp = row
            tmp = tuple(tmp)
            if tmp in row_type:
                row_type[tmp] += 1
            else:
                row_type[tmp] = 1

        return max(row_type.values())
    

class NeetSolution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = collections.defaultdict(int)

        for row in matrix:
            row_key = str(row)

            if row[0]:
                row_key = str([0 if n else 1 for n in row])
            
            count[row_key] += 1

        return max(count.values())