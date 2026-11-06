class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0] * n
        rightMax = -1

        for i in range(n - 1, -1, -1):
            result[i] = rightMax
            rightMax = max(rightMax, arr[i])

        return result
