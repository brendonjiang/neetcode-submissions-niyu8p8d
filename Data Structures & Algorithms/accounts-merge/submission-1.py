from collections import deque
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        result = []
        visits = set()

        def bfs(q, name):
            output = set()

            while q:
                for i in range(len(q)):
                    cur, index = q.popleft()
                    output.add(cur)
                    visits.add(index)

                    for j in range(len(accounts)):
                        if cur in accounts[j] and j not in visits:
                            visits.add(j)
                            
                            for email in accounts[j][1:]:
                                if email != cur:
                                    q.append((email, j))

            return list(output)



        for ind in range(len(accounts)):

            if ind not in visits:
                inp = deque([(email, ind) for email in accounts[ind][1:]])
                output = bfs(inp, accounts[ind][0])
                output.insert(0, accounts[ind][0])
                result.append(output)

        return result
                 





            


            