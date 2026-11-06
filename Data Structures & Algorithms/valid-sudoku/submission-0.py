class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_length = len(board)

        # Check the rows first
        for row in board:
            filtered = list(filter(lambda ele: ele != ".", row))
            if len(set(filtered)) != len(filtered):
                return False

        # Check columns next
        for col in zip(*board):
            filtered = list(filter(lambda ele: ele != ".", col))
            if len(set(filtered)) != len(filtered):
                return False

        # Check 3x3 next
        stride = 3
        for i in range(0, board_length, stride):
            for j in range(0, board_length, stride):
                square = [row[j : j + stride] for row in board[i : i + stride]]
                flattened = [entry for row in square for entry in row]
                filtered = list(filter(lambda ele: ele != ".", flattened))
                if len(set(filtered)) != len(filtered):
                    return False

        return True
