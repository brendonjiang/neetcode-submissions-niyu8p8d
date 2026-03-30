from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if target in deadends or "0000" in deadends:
            return -1

        
        visits = set()

        def bfs(lock):
            q = deque()
            q.append(lock)
            turns = 0

            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    

                    if cur == target:
                        return turns

                    cur = list(cur)

                    for i in range(len(cur)):
                        copy = cur.copy()
                        digit = int(cur[i])

                        copy[i] = str((digit+1) % 10)
                        up = "".join(copy)

                        copy[i] = str((digit-1) % 10)
                        down = "".join(copy)

                        if up not in visits and up not in deadends:
                            visits.add(up)
                            q.append(up)

                        if down not in visits and down not in deadends:
                            visits.add(down)
                            q.append(down)


                turns += 1

            return -1

        
        return bfs("0000")
                    