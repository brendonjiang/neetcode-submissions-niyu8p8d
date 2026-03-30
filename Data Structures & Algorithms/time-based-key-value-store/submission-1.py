from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.myDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myDict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.myDict[key]
        L, R = 0, len(arr)-1
        res = ""

        while L <= R:
            m = (L+R) // 2

            if arr[m][1] <= timestamp:
                res = arr[m][0]
                L = m+1

            else:
                R = m-1

        return res