import heapq
from collections import deque, defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        myDict = defaultdict(int)

        for task in tasks:
            myDict[task] += 1


        heap = [value for value in myDict.values()]
        heapq.heapify_max(heap)

        time = 0

        while heap or queue:
            
            if queue and queue[0][1] == time:
                task = queue.popleft()
                heapq.heappush_max(heap, task[0])
            if not heap and queue[0][1] != time:
                time += queue[0][1] - time
                continue
            time += 1
            cur = heapq.heappop_max(heap)
            cur -= 1

            if cur == 0:
                continue
            
            else:
                queue.append([cur, time + n])

            
        return time



