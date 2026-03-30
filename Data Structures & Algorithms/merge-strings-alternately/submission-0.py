class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L, R = 0, 0
        output = ""


        while L < len(word1) and R < len(word2):
            output += word1[L]
            output += word2[R]

            L += 1
            R += 1

        if L < len(word1):
            output += word1[L:]

        elif R < len(word2):
            output += word2[R:]

        return output