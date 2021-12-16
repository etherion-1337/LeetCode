class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = 0
        for i in operations:
            if i == "X++" or i == "++X":
                ans += 1
            else:
                ans -= 1
        return ans

if __name__ == "__main__":
    soln = Solution()
    _input = ["--X","X++","X++"]
    answer = soln.finalValueAfterOperations(_input)
    print(answer)