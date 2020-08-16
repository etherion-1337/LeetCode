from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for x, y in zip(nums[:n], nums[n:]):
            ans.append(x)
            ans.append(y)

        return ans

if __name__ == "__main__":
    soln = Solution()
    num_list = [1,2,3,4,5,6,7,8]
    answer = soln.shuffle(num_list, n=4)
    print(answer)