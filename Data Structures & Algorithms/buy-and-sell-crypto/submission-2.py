class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L = 0

        for r in range(len(prices)):
            if prices[r] > prices[L]:
                profit = max(profit, prices[r]-prices[L])

            else:
                L = r

        return profit


