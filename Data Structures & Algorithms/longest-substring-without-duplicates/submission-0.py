class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        mySet = set()

        for R in range(len(s)):
            while s[R] in mySet:
                mySet.remove(s[L])
                L += 1

            mySet.add(s[R])
            length = max(length, R-L+1)


        return length
            