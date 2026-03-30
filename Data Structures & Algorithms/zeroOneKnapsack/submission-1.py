class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}

        def helper(i, remaining):

            if i == len(profit) or remaining <= 0:
                return 0

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            skip = helper(i+1, remaining)
            
            if weight[i] <= remaining:
                take = profit[i] + helper(i+1, remaining - weight[i])

            else:
                take = float("-inf")

            memo[(i, remaining)] = max(skip, take)

            return memo[(i, remaining)]

        
        return helper(0, capacity)