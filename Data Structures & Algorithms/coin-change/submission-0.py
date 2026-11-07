import math


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)  # Initialize the DP space with infinities
        dp[0] = 0  # Base Case

        for amount in range(1, amount + 1):
            for coin in coins:
                if (amount - coin) >= 0:
                    # If amount remains positive after subtracting coin
                    dp[amount] = min(
                        dp[amount], 1 + dp[amount - coin]
                    )  # '1' is the coin count

        return dp[amount] if dp[amount] != math.inf else -1
