from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        code_tmp = code*3

        if k == 0:
            return [0] * len(code)
        elif k > 0:
            for i in range(len(code), 2*len(code)):
                ans.append(sum(code_tmp[i+1:i+k+1]))
        else:
            for i in range(len(code), 2*len(code)):
                ans.append(sum(code_tmp[i-1:i+k-1:-1]))
        
        return ans
    
class NeetSolution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        ans = [0] * N

        for i in range(N):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    ans[i] += code[j % N]
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k), -1):
                    ans[i] += code[j % N]
        
        return ans
    
class NeetSolution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        ans = [0] * N

        l = 0
        curr_sum = 0
        for r in range(N + abs(k)):
            curr_sum += code[r % N]

            if r - l + 1 > abs(k):
                curr_sum -= code[l % N]
                l = (l + 1) % N

            if r - l + 1 == abs(k):
                if k > 0:
                    ans[(l - 1) % N] = curr_sum
                elif k < 0:
                    ans[(r + 1) % N] = curr_sum

        return ans