class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L, R = 0, 1

        while R < len(prices):
            if prices[L] > prices[R]:
                L = R

            else:
                cur_profit = prices[R] - prices[L]
                profit = max(cur_profit, profit)
            R += 1

        return profit