class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_counts = {}  # Initialize the dictionary

        # Store frequencies in the dictionary
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        # Sort dictionary in descending order based on frequency
        # num_counts = dict(sorted(num_counts.items(), key=lambda item: item[1], reverse=True))

        # Get the keys of the newly sorted dictionary
        # elements = list(num_counts.keys())

        # return elements[0:k]

        # OR, maintain a min-heap
        heap = []
        for num, count in num_counts.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
