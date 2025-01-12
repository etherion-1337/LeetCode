class Solution:
    """
    stack solution

    time complexity: O(n)
    space complexity: O(n)
    """
    def canBeValid(self, s: str, locked: str) -> bool:
        # track for wild card
        stack_unlocked = []
        # track for locked "("
        stack_locked = []

        # check if every ")" can be closed
        for i in range(len(s)):
            if locked[i] == "0":
                stack_unlocked.append(i)
            else:
                if s[i] == "(":
                    stack_locked.append(i)
                else: # use "("" then wildcard 
                    if stack_locked:
                        stack_locked.pop()
                    elif stack_unlocked:
                        stack_unlocked.pop()
                    else:
                        return False
        
        # check if all "(" can be closed by wildcard
        while stack_unlocked and stack_locked and stack_unlocked[-1] > stack_locked[-1]:
            stack_unlocked.pop()
            stack_locked.pop()

        if stack_locked or len(stack_unlocked) % 2:
            return False
        else:
            return True