import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        i = 0
        initLen = len(nums)

        while i < initLen:
            removedElem = nums.pop(0)
            answer.append(math.prod(nums))
            nums.append(removedElem)
            i += 1

        return answer
