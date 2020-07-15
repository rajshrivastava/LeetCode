class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.product_price_dict = dict()
        for product, price in zip(products, prices):
            self.product_price_dict[product] = price
        self.counter = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter += 1
        bill = 0
        for prod, n in zip(product, amount):
            bill += self.product_price_dict[prod]*n
        if self.counter == self.n:
            bill = bill - (self.discount*bill)/100
            self.counter = 0
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
