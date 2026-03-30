
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = defaultdict(int)
        mapT = defaultdict(int)

        for char in s:
            mapS[char] += 1
        
        for char in t:
            mapT[char] += 1

        for key, value in mapS.items():
            if (key, value) not in mapT.items():
                return False

        for key, value in mapT.items():
            if (key, value) not in mapS.items():
                return False

        return True