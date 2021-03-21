class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = [None]*maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top+1 < self.maxSize:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        else:
            self.top -= 1
            return self.stack[self.top+1]

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i<=self.top:
                self.stack[i] += val
            else:
                break


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
