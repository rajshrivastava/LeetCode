class StockSpanner:

    def __init__(self):
        self.arr = []
        self.firstLargestIndex = []
        self.i = -1

    def next(self, price: int) -> int:
        self.arr.append(price)
        self.i += 1
        
        j = self.i - 1
        while self.arr[j] <= price and j >= 0:
            j = self.firstLargestIndex[j]
        
        self.firstLargestIndex.append(j)
        return self.i - j
      
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
