import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        result = []
        heap = []

        for point in points:
            distance_to_origin = self.euclidean_distance(point)
            heapq.heappush(heap, (distance_to_origin, point))

        for _ in range(k):
            _, point = heapq.heappop(heap)
            result.append(point)

        return result

    def euclidean_distance(self, point: list[int]) -> float:
        x1, y1 = point
        x2, y2 = 0, 0

        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
