from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for s in s1:
            dict1[s] += 1

        L = 0

        for R in range(len(s2)):
            
            while (R-L+1) > len(s1):
                if dict2[s2[L]] != 1:
                    dict2[s2[L]] -= 1
                else:
                    dict2.pop(s2[L])
                L += 1

            dict2[s2[R]] += 1
            
   
            if dict1 == dict2:
                return True
            

        return False