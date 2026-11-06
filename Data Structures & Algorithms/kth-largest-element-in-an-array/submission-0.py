class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kthLargest = 0

        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        for _ in range(k):
            kthLargest = -heapq.heappop(maxHeap)

        return kthLargest
