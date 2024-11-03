class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        
        goal_double = goal + goal

        if s in goal_double:
            return True
        else:
            return False
        
class Solution:
    """
    double s instead of goal
    """
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths are different
        if len(s) != len(goal):
            return False

        # Create a new string by concatenating 's' with itself
        doubled_string = s + s

        # Use find to search for 'goal' in 'doubledString'
        # If find returns an index that is not -1
        # then 'goal' is a substring
        return doubled_string.find(goal) != -1
    
class Solution:
    """
    brute force
    time complexity: O(n^2)
    space complexity: O(1)
    """
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        length = len(s)

        # Try all possible rotations of the string
        for _ in range(length):
            # Perform one rotation
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False