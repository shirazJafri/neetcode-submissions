class Solution:
    def findMin(self, nums: list[int]) -> int:
        result = 5000
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                # We are in a sorted portion of the array
                result = min(result, nums[left])
                break

            # We are in the rotated array
            mid = (left + right) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[left]:
                # We need to look at the right subportion
                left = mid + 1
            else:
                # We need to look at the left subportion
                right = mid - 1

        return result
