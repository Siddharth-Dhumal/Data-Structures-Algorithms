class MyHashMap:

    def __init__(self):
        self.h_map = []

    def put(self, key: int, value: int) -> None:
        for arr in self.h_map:
            if arr[0] == key:
                arr[1] = value
                return
        
        self.h_map.append([key, value])

    def get(self, key: int) -> int:
        for arr in self.h_map:
            if arr[0] == key:
                return arr[1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.h_map)):
            if self.h_map[i][0] == key:
                self.h_map.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)