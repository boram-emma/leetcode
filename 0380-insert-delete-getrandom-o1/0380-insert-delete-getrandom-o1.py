class RandomizedSet:

    def __init__(self):
        self.sset = set()

    def insert(self, val: int) -> bool:
        if val in self.sset:
            return False
        else:
            self.sset.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.sset:
            self.sset.remove(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        return random.sample(list(self.sset), 1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()