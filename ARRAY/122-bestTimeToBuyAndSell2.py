class Solution:
    def maxProfit(self, prices) -> int:
        max_profit_gain = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                max_profit_gain += (prices[i + 1] - prices[i])
        return max_profit_gain


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    a = Solution()
    print(a.maxProfit(prices))
