class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s_counts = Counter(s)
        t_counts = Counter(t)

        return s_counts == t_counts