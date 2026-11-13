class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            if num == 0:
                # If we encounter a 0, reset count and update result
                result = max(result, count)
                count = 0
            else:
                count = count + 1

        # Return max because it's not guaranteed that nums end with a 0
        return max(result, count)
