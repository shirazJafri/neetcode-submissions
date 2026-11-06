from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        minutes = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while fresh_oranges > 0 and queue:
            queue_len = len(queue)
            for i in range(queue_len):
                row, col = queue.popleft()

                for dr_row, dr_col in directions:
                    new_row, new_col = row + dr_row, col + dr_col
                    within_bounds = new_row in range(ROWS) and new_col in range(COLS)

                    if within_bounds and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh_oranges -= 1
                        queue.append((new_row, new_col))

            minutes += 1
        return minutes if fresh_oranges == 0 else -1
