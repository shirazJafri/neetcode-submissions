from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build an adjacency list with a hashmap: {node -> [edges]}
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        min_heap = [(0, k)]  # Min Heap to run BFS
        time = (
            0  # To keep track of the time it takes for all nodes to receive the signal
        )
        visited = (
            set()
        )  # To keep track of which nodes have already been visited, to avoid cycles

        while min_heap:
            weight_heap, node = heapq.heappop(min_heap)
            if node in visited:
                continue  # Node already visited, proceed with other nodes
            visited.add(node)  # Mark node as visited
            time = max(time, weight_heap)

            # Iterate over neighbors of the node
            for vertex, weight in edges[node]:
                if vertex not in visited:
                    heapq.heappush(min_heap, (weight_heap + weight, vertex))

        return -1 if len(visited) != n else time
