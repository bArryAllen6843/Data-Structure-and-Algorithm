import math


class Solution:
    #  Bottom up DP
    def coinChange(self, coins, amount: int) -> int:
        n = len(coins)
        dp = [[math.inf] * (amount + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0
            for amnt in range(1, amount + 1):
                if i >= 0:
                    dp[i][amnt] = dp[i - 1][amnt]  # Skip i_th coin
                if amnt >= coins[i]:
                    dp[i][amnt] = min(dp[i][amnt], dp[i][amnt - coins[i]] + 1)  # Use i_th coin

        return dp[n - 1][amount] if dp[n - 1][amount] != math.inf else -1

    # Bottom up DP (Space Optimized)
    def coinChange1(self, coins, amount: int) -> int:
        n = len(coins)
        coins.sort()
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for amnt in range(1, amount + 1):
            for coin in coins:
                if amnt >= coin:
                    dp[amnt] = min(dp[amnt], dp[amnt - coin] + 1)
                else:
                    break
        return dp[amount] if dp[amount] != math.inf else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    a = Solution()
    print(a.coinChange(coins, amount))

    print(a.coinChange1(coins, amount))
