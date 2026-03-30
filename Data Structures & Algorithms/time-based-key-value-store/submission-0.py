from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.myDict = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myDict:
            self.myDict[key] = []
        self.myDict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.myDict:
            return res
        L, R = 0, len(self.myDict[key])-1

        while L <= R:
            m = (L+R) // 2

            if self.myDict[key][m][1] > timestamp:
                R = m-1

            elif self.myDict[key][m][1] < timestamp:
                res = self.myDict[key][m][0]
                L = m+1

            else:
                return self.myDict[key][m][0]

        return res