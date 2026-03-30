class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        counts = Counter(s)
        counts2 = Counter(t)

        return counts == counts2
        