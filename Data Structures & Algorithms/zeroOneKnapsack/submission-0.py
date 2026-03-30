class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def helper(i, remaining):

            if i == len(profit) or remaining <= 0:
                return 0

            
            skip = helper(i+1, remaining)
            
            if weight[i] <= remaining:
                take = profit[i] + helper(i+1, remaining - weight[i])

            else:
                take = float("-inf")

            return max(skip, take)

        
        return helper(0, capacity)