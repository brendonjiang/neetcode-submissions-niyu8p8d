class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        mySet = set()

        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[L])
                L += 1

            mySet.add(s[r])

            length = max(length, r-L+1)

        return length