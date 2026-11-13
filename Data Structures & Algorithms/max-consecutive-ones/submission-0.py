class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_consecutive_ones = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                # denotes start of a sequence so update left
                left = right

                # expand window until a zero is encountered
                while right < len(nums) and nums[right] != 0:
                    right = right + 1
                max_consecutive_ones = max(max_consecutive_ones, (right - left))

        return max_consecutive_ones
