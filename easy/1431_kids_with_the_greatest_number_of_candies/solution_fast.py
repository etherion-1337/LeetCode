from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        threshold = max(candies) - extraCandies

        return [i >= threshold for i in candies]


if __name__ == "__main__":
    soln = Solution()
    candy_list = [1,2,3,4,4,7]
    answer = soln.kidsWithCandies(candies = candy_list, extraCandies = 2)
    print(answer)