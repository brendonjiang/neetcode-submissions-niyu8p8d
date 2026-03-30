class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            this_profit = prices[i] - min(prices[:i])
            if this_profit > profit:
                profit = this_profit
        return profit

