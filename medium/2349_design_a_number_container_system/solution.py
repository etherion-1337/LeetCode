from sortedcontainers import SortedList
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.idx2num = {} # idx -> number
        self.num2idx = defaultdict(lambda: SortedList()) # num -> list of idx

    def change(self, index: int, number: int) -> None:
        if index in self.idx2num:
            prev = self.idx2num[index]
            self.num2idx[prev].remove(index)
        
        self.idx2num[index] = number
        self.num2idx[number].add(index)

    def find(self, number: int) -> int:
        if len(self.num2idx[number]) == 0:
            return -1
        else:
            return self.num2idx[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)