

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


if __name__ == "__main__":
    soln = Solution()
    address = "255.100.50.0"
    answer = soln.defangIPaddr(address)
    print(answer)