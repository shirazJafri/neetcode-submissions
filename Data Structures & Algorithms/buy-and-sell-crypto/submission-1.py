class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                # High buying, and low selling i.e. no profit
                left = right
            else:
                # High selling, low buying i.e. profit
                max_profit = max(max_profit, prices[right] - prices[left])

        return max_profit
