class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        # not <= because same element cannot be used twice
        while left < right:
            sum_left_right = numbers[left] + numbers[right]

            if sum_left_right == target:
                return [left + 1, right + 1]  # 1-indexed array
            elif sum_left_right > target:
                right = right - 1
            else:
                left = left + 1

        return []  # dummy return since 1 solution is guaranteed
