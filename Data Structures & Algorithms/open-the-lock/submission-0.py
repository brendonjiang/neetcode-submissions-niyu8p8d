from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        deadends = set(deadends)

        visits = set()
        
        turns = 0

        q = deque(["0000"])

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                visits.add(cur)
                
                if cur == target:
                    return turns

                cur_copy = cur

                for i in range(0, len(cur)):
                    up, down = str((int(cur[i])+1) % 10), str((int(cur[i])-1) % 10)
                    
                    cur = list(cur)
                    cur[i] = up

                    if "".join(cur) not in visits and "".join(cur) not in deadends:
                        visits.add("".join(cur))
                        q.append("".join(cur))
                    
                    cur[i] = down
                    if "".join(cur) not in visits and "".join(cur) not in deadends:
                        visits.add("".join(cur))
                        q.append("".join(cur))

                    cur = cur_copy
                    
                    

            turns += 1
                    

                
        
        return -1

            