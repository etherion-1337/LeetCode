class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        index_list = [keyboard.index(x) for x in word]
        ans_list = []
        for i in range(len(index_list)-1):
            ans_list.append(abs(index_list[i]-index_list[i+1]))
        ans = sum(ans_list) + index_list[0]
        return ans

if __name__ == "__main__":
    soln = Solution()
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "cba"
    answer = soln.calculateTime(keyboard, word)
    print(answer)