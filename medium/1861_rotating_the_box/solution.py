from typing import List

class Solution:
    """
    in-place solution

    time complexity: O(ROWS * COLS)
    space complexity: O(1)
    """
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box), len(box[0])

        # move stones to the next available position on the right
        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == "*": # obstacle, move pointer to the left of the obstacle
                    i = c - 1

        ans = []

        for c in range(COLS):
            col = [] # this is row after rotation
            for r in reversed(range(ROWS)):
                col.append(box[r][c])
            ans.append(col)

        return ans
    

class Solution:
    """
    not in-place solution
    """
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box), len(box[0])

        ans = [["."] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if box[r][c] == "#":
                    ans[i][ROWS - r - 1] = "#"
                    i -= 1
                elif box[r][c] == "*":
                    ans[c][ROWS - r - 1] = "*"
                    i = c - 1

        return ans