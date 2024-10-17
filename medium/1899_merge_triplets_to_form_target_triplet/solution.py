from typing import List

class Solution:
    """
    Greedy solution

    we first filter out all the triplets that have at least one element greater than the target -> we can't form the target triplet with these
    then we check if target exist in the remaining triplets -> step 1 guarantees that we can form the target triplet with the remaining triplets since all elements are less than or equal to the target

    time complexity: O(n)
    space complexity: O(1)
    """
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = {0: False,
                 1: False,
                 2: False}
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if triplet[0] == target[0]:
                check[0] = True
            if triplet[1] == target[1]:
                check[1] = True
            if triplet[2] == target[2]:
                check[2] = True
        
        return all(value == True for value in check.values())
    

class NeetSolution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3