class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        ans = [first]
        for num in encoded:
            ans.append(num^ans[-1])
        return ans

if __name__ == "__main__":
    soln = Solution()
    _input = [1,2,3]
    first = 1
    answer = soln.decode(_input, first)
    print(answer)