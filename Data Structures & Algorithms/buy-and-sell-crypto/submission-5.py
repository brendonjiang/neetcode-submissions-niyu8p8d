class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_price = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                max_price = max(max_price, price)
                r += 1

            else:
                l = r
                r += 1
            
        return max_price