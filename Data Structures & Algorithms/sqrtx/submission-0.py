class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        res = None

        while L <= R:
            m = (L+R) // 2

            if m ** 2  > x:
                R = m-1

            elif m ** 2 < x:
                L = m+1
                res = m

            else:
                return m

        return res
            
        