from typing import List

class Solution:
    """
    observations:

    1. if matrix has even number of negative numbers, we can always make all numbers positive
    2. if matrix has odd number of negative numbers, we can make all numbers positive except one, except if there is a zero
    3. we can move the negative sign to the smallest absolute value to minimize the sum

    time complexity: O(n*m)
    space complexity: O(1)
    """
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        zero_flag = False
        neg_count = 0
        ans = 0
        min_val = float("inf")

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_flag = True
                elif matrix[r][c] < 0:
                    neg_count += 1
                min_val = min(min_val, abs(matrix[r][c]))
                ans += abs(matrix[r][c])

        if (neg_count % 2 and zero_flag) or neg_count % 2 == 0:
            return ans
        else:
            ans -= min_val*2
            return ans