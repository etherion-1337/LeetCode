from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2*n - 1)
        used = set() # nums already placed

        def backtrack(i): # cur idx
            if i == len(ans):
                return True
            
            # try largest elements
            for num in reversed(range(1, n + 1)):
                # validation
                if num in used:
                    continue
                if num > 1 and (i+num >= len(ans) or ans[i+num]):
                    continue
            
                # try decision
                used.add(num)
                if num == 1:
                    ans[i] = num
                else:
                    ans[i] = num
                    ans[i+num] = num
                
                j = i + 1
                while j < len(ans) and ans[j]: # use while instead of for becos next idx could be taken
                    j += 1
                
                # recursive
                if backtrack(j):
                    return True
            
                # backtrack
                used.remove(num)
                if num == 1:
                    ans[i] = 0
                else:
                    ans[i] = 0
                    ans[i+num] = 0
            return False
        backtrack(0)
        return ans