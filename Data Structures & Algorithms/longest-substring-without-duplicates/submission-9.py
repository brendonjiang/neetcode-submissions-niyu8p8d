class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myWindow = set()

        l, r = 0, 0
        max_length = 0

        while r < len(s):
            while s[r] in myWindow:
                myWindow.remove(s[l])
                l += 1

            myWindow.add(s[r])
            length = r - l + 1
            max_length = max(max_length, length)
            r += 1

        return max_length
