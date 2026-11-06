class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, num in enumerate(nums):
            requiredValue = target - num

            if requiredValue in hashMap:
                return [hashMap[requiredValue], index]

            hashMap[num] = index
        return []
