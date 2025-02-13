import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k :
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k :
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def main():
    k = 3
    nums = [4, 2, 6, 1, 5]
    kth_largest = KthLargest(k, nums)

    val = 7
    result = kth_largest.add(val)
    print(result)

if __name__ == "__main__":
    main()