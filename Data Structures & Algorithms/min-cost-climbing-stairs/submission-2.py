class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minimum = float("inf")
        memo = {}

        def helper(i):
            
            if i in memo:
                return memo[i]

            if i >= len(cost):
                return 0


            memo[i] = min(helper(i+1) + cost[i], helper(i+2) + cost[i])
            return memo[i]

        ans1 = helper(0)
        memo.clear()
        ans2 = helper(1)

        return min(ans1, ans2)