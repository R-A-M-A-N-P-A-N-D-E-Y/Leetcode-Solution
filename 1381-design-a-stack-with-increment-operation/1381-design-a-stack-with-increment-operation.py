class CustomStack:
    n = 0
    stack = []

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)
        

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            ele = self.stack[-1]
            self.stack.pop(-1)
            return ele
        

    def increment(self, k: int, val: int) -> None:
        if k >= self.n:
            for i in range(len(self.stack)):
                self.stack[i] += val
        elif len(self.stack) > k:
            for i in range(k):
                self.stack[i] += val
        else:
            for i in range(len(self.stack)):
                self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)