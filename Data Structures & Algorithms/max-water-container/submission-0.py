class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        l = 0
        r = len(height) - 1

        while l < r:
            width = r - l
            area = min(height[l], height[r]) * width

            if area > maxArea:
                maxArea = area

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxArea
