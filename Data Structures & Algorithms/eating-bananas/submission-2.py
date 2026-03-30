import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        
        output = max(piles)
        while L <= R:
            m = (L+R) // 2
            total = 0
            for num in piles:
                total += math.ceil(num / m)

            if total <= h:
                output = min(output, m)
                R = m-1
            else:
                L = m+1
        return output