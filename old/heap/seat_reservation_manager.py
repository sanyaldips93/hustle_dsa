import heapq


class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [i+1 for i in range(n)]
        

    def reserve(self) -> int:
        return heapq.heappop(self.unreserved)
        
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)
            
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)