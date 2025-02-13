class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        cur = self.stack
        while cur and cur[-1][0] <= price:
            [_, val] = cur.pop()
            span += val
        cur.append([price, span])
        return span


        


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
arr = [100, 80, 60, 70, 60, 75, 85]
for ele in arr:
    print(obj.next(ele))
