from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        myDict = defaultdict(int)
        max_window = 0

        for r in range(len(s)):
            myDict[s[r]] += 1
            max_count = 0
            for key, value in myDict.items():
                max_count = max(max_count, value)

            available = (r - L + 1) - max_count
            
            while available > k:
                myDict[s[L]] -= 1
                L += 1
                for key, value in myDict.items():
                    max_count = max(max_count, value)
                available = (r - L + 1) - max_count
                
            max_window = max(max_window, r-L+1)

        return max_window
            


            