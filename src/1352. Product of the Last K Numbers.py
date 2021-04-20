class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        self.i = 0
        
    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
            self.i = 0        
        else:
            self.arr.append(self.arr[-1]*num)
            self.i += 1

    def getProduct(self, k: int) -> int:
        if k > self.i:
            return 0
        return self.arr[-1]//self.arr[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
