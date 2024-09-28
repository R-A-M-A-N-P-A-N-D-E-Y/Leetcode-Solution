class MyCircularDeque:
    n = 0
    queue = []
    cnt = 0

    def __init__(self, k: int):
        self.n = k
        self.queue = []
        self.cnt = 0

    def insertFront(self, value: int) -> bool:
        if self.cnt < self.n :
            self.queue.insert(0, value)
            self.cnt += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.cnt < self.n :
            self.queue.insert(self.cnt, value)
            self.cnt += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.cnt != 0 :
            self.queue.pop(0)
            self.cnt -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.cnt != 0 :
            self.queue.pop(-1)
            self.cnt -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.cnt != 0 :
            return self.queue[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.cnt != 0 :
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.cnt == 0 :
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.cnt == self.n :
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()