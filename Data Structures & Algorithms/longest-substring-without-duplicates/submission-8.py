class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        longest = 0
        L = 0

        for R in range(len(s)):
            if s[R] in mySet:
                while s[R] in mySet:
                    mySet.remove(s[L])
                    L += 1

            mySet.add(s[R])
            longest = max(longest, R-L)
        
            
        return longest+1 if len(s) > 0 else 0