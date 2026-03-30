class StockSpanner:

    def __init__(self):
        self.time = 0
        self.stack = []


    def next(self, price: int) -> int:
        self.time += 1

        copy = self.stack.copy()
        
        span = 0
        while copy and price >= copy[-1][0]:
            span = self.time - copy[-1][1]
            copy.pop()

        self.stack.append((price, self.time))
        return span + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)