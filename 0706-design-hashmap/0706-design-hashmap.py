class MyHashMap:

    def __init__(self):
        self.ls = {}

    def put(self, key: int, value: int) -> None:
            self.ls[key] = value

    def get(self, key: int) -> int:
        if key in self.ls:
            return self.ls[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.ls:
            del self.ls[key]
        else:
            return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)