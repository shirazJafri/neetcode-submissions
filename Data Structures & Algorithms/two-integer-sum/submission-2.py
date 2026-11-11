class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # num => index

        for idx, num in enumerate(nums):
            # One can consider duplicates but since there only exists one solution
            # and can be returned in any order, we can overwrite the index value.
            if (target - num) in hash_map:
                key = target - num
                return [hash_map[key], idx]

            hash_map[num] = idx

        return []
