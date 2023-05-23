class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [] 
    
        for num in nums:
            self.add(num)
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) 
        if len(self.heap) > self.k:
            heapq.heappop(self.heap) 
        return self.heap[0]
