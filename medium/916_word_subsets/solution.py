from collections import Counter
from typing import List
from collections import defaultdict

class Solution:
    """
    brute force solution
    """
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def is_subset(str1, str2):
            """
            str1 is a subset of str2 or not
            """
            i = j = 0
            if len(str1) > len(str2):
                return False
            freq = Counter(str2)
            
            for c in str1:
                freq[c] -= 1
            if any(v < 0 for v in freq.values()):
                return False
            else:
                return True

        ans = []

        for w1 in words1:
            flag = [0]*len(words2)
            for k in range(len(words2)):
                if is_subset(words2[k], w1):
                    flag[k] = 1
            if sum(flag) == len(words2):
                ans.append(w1) 

        return ans
    

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)

        for w in words2:
            count_w = Counter(w)
            for char, count in count_w.items():
                count_2[char] = max(count_2[char], count)

        ans = []

        for w in words1:
            count_w = Counter(w)
            flag = True
            for char, count in count_2.items():
                if count_w[char] < count:
                    flag = False
                    break
            if flag:
                ans.append(w)

        return ans