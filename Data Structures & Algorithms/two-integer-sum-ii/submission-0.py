class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_1 = 0
        index_2 = len(numbers) - 1

        while index_1 < index_2:
            s = numbers[index_1] + numbers[index_2]
            if s == target:
                return [index_1 + 1, index_2 + 1]
            elif s > target:
                index_2 -= 1
            else:
                index_1 += 1

        return []
