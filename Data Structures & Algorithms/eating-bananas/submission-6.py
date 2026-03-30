import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)

        minBananas = max(piles)

        while L <= R:

            m = (L+R) // 2
            total = 0

            for n in piles:
                total += math.ceil(n / m)

            if total > h:
                L = m+1

            if total <= h:
                R = m-1
                minBananas = min(m, minBananas)


        return minBananas
        