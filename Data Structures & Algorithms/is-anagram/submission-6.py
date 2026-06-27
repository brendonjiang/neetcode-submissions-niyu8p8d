class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counter(word):
            from collections import defaultdict

            counts = defaultdict(int)

            for char in word:
                counts[char] += 1

            return counts

        return counter(s) == counter(t)