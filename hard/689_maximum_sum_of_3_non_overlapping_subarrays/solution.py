from typing import List

class NeetSolution:
    """
    DP solution
    """
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # sum of length k end at at index i
        k_sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] - nums[i - k] + nums[i])

        dp = {}
        def get_max_sum(i, cnt):
            if cnt == 3 or i > len(nums) - k:
                return 0
            if (i, cnt) in dp:
                return dp[(i, cnt)]

            # include current element
            include = k_sums[i] + get_max_sum(i + k, cnt + 1)
            # skip current element
            skip = get_max_sum(i + 1, cnt)

            dp[(i, cnt)] = max(include, skip)
            return dp[(i, cnt)]

        def get_ind():
            i = 0
            ind = []

            while i <= len(nums) and len(ind) < 3:
                include = k_sums[i] + get_max_sum(i + k, len(ind) + 1)
                skip = get_max_sum(i + 1, len(ind))

                if include >= skip:
                    ind.append(i)
                    i += k
                else:
                    i += 1
                    
            return ind
        
        return get_ind()