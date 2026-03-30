class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length = len(pref)
        counter = 0

        for word in words:
            if word[:length] == pref:
                counter += 1

            
        return counter