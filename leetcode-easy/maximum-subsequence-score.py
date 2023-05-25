class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums1, nums2))
        pairs = sorted(pairs, key= lambda p:p[1], reverse = True)

        minHeap =[] 
        n1sum = 0
        res = 0

        for n1, n2 in pairs:
            n1sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                popped = heapq.heappop(minHeap)
                n1sum -= popped
            if len(minHeap) == k:
                res = max(res, n1sum * n2)
        return res