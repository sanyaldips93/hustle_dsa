import heapq


class MedianFinder:

    def __init__(self):
        # two heaps are required. small will be a maxheap and large will be a minheap
        # heaps should be of equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # add to the small heap by default
        heapq.heappush(self.small, -1 * num)

        # check if the largest value in small heap is greater than smallest val in min heap
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # check if both the sizes of heaps do not differ by more than 1
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()