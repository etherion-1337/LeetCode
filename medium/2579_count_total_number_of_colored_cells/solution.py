class Solution:
    def coloredCells(self, n: int) -> int:
        # n = 1    +0 1
        # n = 2    +4 5
        # n = 3    +4 +4 13
        # n = 4    +4 +4 +4 25 

        n_4 = n - 1 # largest num of +4 at n
        tri_num = (n_4**2 + n_4)/2 # total num of +4
        ans = 1 + tri_num*4

        return int(ans)
    
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4*(n*(n-1)//2)
    

class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        for i in range(n):
            ans += (4*i)

        return ans