class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check row
        for i in range(9):
            filled_row = [num for num in board[i] if num != "."]
            if len(filled_row) != len(set(filled_row)):
                return False

        # check col
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            filled_col = [num for num in col if num != "."]
            if len(filled_col) != len(set(filled_col)):
                return False

        # check subbox
        box_corner = [[[0,2],[0,2]],[[3,5],[0,2]],[[6,8],[0,2]],[[0,2],[3,5]], [[3,5],[3,5]],[[6,8],[3,5]],[[0,2],[6,8]],[[3,5],[6,8]],[[6,8],[6,8]]]

        for box in box_corner:
            box_nums = []
            for i in range(box[0][0],box[0][1]+1):
                for j in range(box[1][0], box[1][1]+1):
                    box_nums.append(board[i][j])
            filled_box = [num for num in box_nums if num != "."]
            if len(filled_box) != len(set(filled_box)):
                return False
        
        return True
