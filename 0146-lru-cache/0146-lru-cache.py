class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.counter = []
        self.n = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.counter.remove(key)
            self.counter.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.counter.remove(key)
            self.counter.append(key)
        else:
            if len(self.cache) == self.n:
                lru = self.counter.pop(0)
                del self.cache[lru]

            self.cache[key] = value
            self.counter.append(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)