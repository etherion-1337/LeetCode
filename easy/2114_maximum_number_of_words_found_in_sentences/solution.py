class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans = max([len(s.split()) for s in sentences])
        return ans

if __name__ == "__main__":
    obj = Solution()
    _input_1 = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
    answer = obj.mostWordsFound(_input_1)
    print(answer)