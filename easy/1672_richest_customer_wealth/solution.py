from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        list_sum = [sum(acc) for acc in accounts]
        return max(list_sum)

if __name__ == "__main__":
    soln = Solution()
    account = [[1,2,3],[3,2,1]]
    answer = soln.maximumWealth(account)
    print(answer)
