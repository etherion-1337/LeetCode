class Solution:
    """
    Two pointers

    time complexity: O(n)
    space complexity: O(1)
    """
    def canChange(self, start: str, target: str) -> bool:
        start_idx = 0
        target_idx = 0

        if len(start) != len(target):
            return False

        while start_idx < len(start) or target_idx < len(target):
            while start_idx < len(start) and start[start_idx] == "_":
                start_idx += 1
            while target_idx < len(start) and target[target_idx] == "_":
                target_idx += 1
            # if all the characters are "_", return True
            if start_idx == len(start) and target_idx == len(target):
                return True
            # one of the string has reached the end but the other one hasn't
            if start_idx == len(start) or target_idx == len(target):
                return False
            # consider the order of "L" and "R"
            if (start[start_idx] != target[target_idx] or (start[start_idx] == "L" and start_idx < target_idx) or (start[start_idx] == "R" and start_idx > target_idx)):
                return False
            
            start_idx += 1
            target_idx += 1


        return True