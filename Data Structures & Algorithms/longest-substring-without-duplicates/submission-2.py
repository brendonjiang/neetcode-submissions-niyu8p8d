class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()

        L = 0
        length = 0
        max_length = 0
        
        for i in range(len(s)):
            
            
            while s[i] in mySet:
                mySet.remove(s[L])
                L += 1
                length -= 1

            
            mySet.add(s[i])
            length += 1
            max_length = max(length, max_length)

        return max_length