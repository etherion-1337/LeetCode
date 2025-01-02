from typing import List

class Solution:
    """
    prefix sum

    time complexity: O(n)
    space complexity: O(n)
    """
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def check_valid(word):
            if word[0] in ["a", "e", "i", "o", "u"] and word[-1] in ["a", "e", "i", "o", "u"]:
                return True

        tmp = [1 if check_valid(word) else 0 for word in words]

        prefix_sum = []
        curr_sum = 0
        for _tmp in tmp:
            curr_sum += _tmp
            prefix_sum.append(curr_sum)
        prefix_sum = [0] + prefix_sum + [prefix_sum[-1]]
        ans = []

        for start, end in queries:
            ans.append(prefix_sum[end + 1] - prefix_sum[start])

        return ans
    

class NeetSolution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_set = set("aeiou")

        prefix_cnt = [0] * (len(words) + 1)
        prev = 0

        for i, w in enumerate(words):
            if w[0] in vowel_set and w[-1] in vowel_set:
                prev += 1
            prefix_cnt[i + 1] = prev

        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            ans[i] = prefix_cnt[r + 1] - prefix_cnt[l]
        return ans