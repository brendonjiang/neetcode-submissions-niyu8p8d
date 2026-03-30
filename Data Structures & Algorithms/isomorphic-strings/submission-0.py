class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        myMap = {}

        for i in range(len(s)):
            if (s[i] in myMap and myMap[s[i]] != t[i]) or (s[i] not in myMap and t[i] in myMap.values()):
                return False
            else:
                myMap[s[i]] = t[i]

        return True