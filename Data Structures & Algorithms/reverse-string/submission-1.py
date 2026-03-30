class Solution:
    def reverseString(self, s: List[str]) -> None:
        L = 0
        R = len(s)-1

        while L < R:
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1
        return s
        