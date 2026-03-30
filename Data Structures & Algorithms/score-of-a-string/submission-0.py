class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        total = 0

        for j in range(1, len(s)):
            total += abs(ord(s[j])-ord(s[i]))
            i += 1


        return total