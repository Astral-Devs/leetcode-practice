import random
class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False

        self.dic[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        loc = self.dic[val]
        self.dic[self.arr[-1]] = loc

        self.arr[loc], self.arr[-1] = self.arr[-1],self.arr[loc]

        self.arr.pop()
        del self.dic[val]

        return True

    def getRandom(self) -> int:

        return random.choice(self.arr)
