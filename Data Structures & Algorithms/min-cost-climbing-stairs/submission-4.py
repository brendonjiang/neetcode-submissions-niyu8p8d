class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        memo2 = {}

        def helper(i, memo):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0

            memo[i] = min(helper(i+1, memo)+cost[i], cost[i]+helper(i+2, memo))
            return memo[i]

        

        return min(helper(0, memo), helper(1, memo2))