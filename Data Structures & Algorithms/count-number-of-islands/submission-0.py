class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Potential directions one can move into
        # [1, 0] --> horizontal right, [-1, 0] --> horizontal left
        # [0, 1] --> vertical down, [0, -1] --> vertical up
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            out_of_bounds = (row < 0 or col < 0) or (row >= ROWS or col >= COLS)

            # Out of bounds OR (already visited OR water as neighbor)
            if out_of_bounds or grid[row][col] == "0":
                return

            # Mark the current row and column as visited i.e. mark it as water
            grid[row][col] = "0"

            # Iterate over all possible directions to check for connected land parts
            for direction_row, direction_column in directions:
                dfs(row + direction_row, col + direction_column)

        # Iterate over the grid... When a land piece found, run a graph algo to get connected components
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1

        return islands
