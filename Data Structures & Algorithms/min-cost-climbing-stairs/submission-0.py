class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minimum = float("inf")
        

        def helper(i, total):
            nonlocal minimum
            
            
            if i >= len(cost):
                minimum = min(minimum, total)
                return

            
            helper(i+1, total+cost[i])
            helper(i+2, total+cost[i])

            return

        helper(0, 0)
        helper(1, 0)

        return minimum