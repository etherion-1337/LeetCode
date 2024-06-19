class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = s.split()
        concat_str = "".join(s_list)
        alpha_num_str = ""
        for char in concat_str:
            if char.isalnum():
                alpha_num_str += char.lower()

        i = 0
        j = len(alpha_num_str)-1

        while j > i:
            if alpha_num_str[i] != alpha_num_str[j]:
                print(i)
                print(j)
                return False
            i += 1
            j -= 1

        return True
    
    