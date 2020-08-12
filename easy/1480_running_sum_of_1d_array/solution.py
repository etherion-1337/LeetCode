from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        prev_ans = 0
        
        for num in nums:
            curr_ans = num + prev_ans
            ans.append(curr_ans)
            prev_ans = curr_ans
            
        return ans

if __name__ == "__main__":
    soln = Solution()
    num_list = [1,2,3,4]
    answer = soln.runningSum(num_list)
    print(answer)