class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        zip_list = list(zip(list(s), indices))
        zip_list.sort(key=lambda x: x[1])
        ans = "".join([i[0] for i in zip_list])
        return ans

if __name__ == "__main__":
    obj = Solution()
    _input_1 = "codeleet"
    _input_2 = [4,5,6,7,0,2,1,3]
    answer = obj.restoreString(_input_1, _input_2)
    print(answer)