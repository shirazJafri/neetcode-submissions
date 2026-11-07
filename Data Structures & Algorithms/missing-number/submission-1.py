class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        set_of_all_nums = set(range(n + 1))
        set_of_nums = set(nums)

        difference = set_of_all_nums.difference(set_of_nums)

        return difference.pop()
