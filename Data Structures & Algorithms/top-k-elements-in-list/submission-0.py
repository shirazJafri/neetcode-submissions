class Solution:
    def getSortedNumCounts(self, nums: List[int]) -> List[tuple]:
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        return sorted(hashMap.items(), key=lambda x: x[1], reverse=True)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedNumCounts = self.getSortedNumCounts(nums)

        return [sortedNum[0] for sortedNum in sortedNumCounts[0:k]]
