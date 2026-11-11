class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)  # no. of rows
        n = len(matrix[0])  # no. of columns

        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) // 2

            # get (i, j) from the mid index
            i = mid // n
            j = mid % n

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
