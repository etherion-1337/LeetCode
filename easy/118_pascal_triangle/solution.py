from typing import List

class Solution:
    """
    time complexity: O(n^2)
    space complexity: O(n^2)
    """
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        
        for i in range(1, numRows):
            tmp = [0] + ans[-1] + [0]
            tmp_ans = []
            for i in range(len(tmp)-1):
                tmp_ans.append(tmp[i]+tmp[i+1])
            ans.append(tmp_ans)
        
        return ans
    
class NeetSolution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        
        return res


class NeetSolution:
    """
    recursive solution
    """
    def generate(self, rowIndex) -> List[List[int]]:
        if rowIndex == 0:
            return [[1]]
        else:
            return self.getAllRow(rowIndex - 1)

    def getAllRow(self, rowIndex):
        if rowIndex == 0:
            return [[1]]
        ListPrec = self.getAllRow(rowIndex - 1)
        Len = len(ListPrec[-1])
        ListPrec.append([1])
        for i in range(0, Len - 1):
            ListPrec[-1].append(ListPrec[-2][i] + ListPrec[-2][i + 1])
        ListPrec[-1].append(1)
        return ListPrec