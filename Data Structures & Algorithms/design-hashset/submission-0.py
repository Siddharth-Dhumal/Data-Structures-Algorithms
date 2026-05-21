class MyHashSet:

    def __init__(self):
        self.h_set = []

    def add(self, key: int) -> None:
        if key not in self.h_set:
            self.h_set.append(key)

    def remove(self, key: int) -> None:
        index = 0
        for i in range(len(self.h_set)):
            if self.h_set[i] != key:
                self.h_set[index] = self.h_set[i]
                index += 1
        if len(self.h_set) > index:
            self.h_set.pop()

    def contains(self, key: int) -> bool:
        return True if key in self.h_set else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)