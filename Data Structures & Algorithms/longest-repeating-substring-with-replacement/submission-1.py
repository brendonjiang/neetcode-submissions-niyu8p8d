from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        myDict = defaultdict(int)
        max_window = 0
        max_count = 0

        for r in range(len(s)):
            myDict[s[r]] += 1
            max_count = max(myDict[s[r]], max_count)

            while (r-L+1) - max_count > k:
                myDict[s[L]] -= 1
                L += 1

            max_window = max(max_window, r-L+1)

        return max_window


            