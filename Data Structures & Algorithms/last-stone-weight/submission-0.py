class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        maxHeap = [-weight for weight in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, -(y - x))

        return 0 if not maxHeap else -heapq.heappop(maxHeap)
