class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if key in self.set:
            idx = self.set.index(key)
            del self.set[idx]
        

    def contains(self, key: int) -> bool:
        if key in self.set:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)