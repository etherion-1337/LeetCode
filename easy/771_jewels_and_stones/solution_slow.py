class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for j in J:
            for s in S:
                if j == s:
                    count += 1
        return count


if __name__ == "__main__":
    soln = Solution()
    J = "aA"
    S = "aAAbbbb"
    answer = soln.numJewelsInStones(J,S)
    print(answer)