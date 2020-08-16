from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= max_value:
                candies[i] = True
            else:
                candies[i] = False
        
        return candies


if __name__ == "__main__":
    soln = Solution()
    candy_list = [1,2,3,4,4,7]
    answer = soln.kidsWithCandies(candies = candy_list, extraCandies = 2)
    print(answer)