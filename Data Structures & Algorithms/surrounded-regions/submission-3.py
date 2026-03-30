from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        def bfs(q):
            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    board[r][c] = "T"

                    for dr, dc in neighbors:
                        nr, nc = dr+r, dc+c

                        if min(nr, nc) < 0 or nr == rows or nc == cols or board[nr][nc] == "T" or board[nr][nc] == "X":
                            continue

                        q.append((nr, nc))

            return

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "O" or (1 <= r <= len(board)-2 and 1 <= c <= len(board[0])-2):
                    continue
                
                else:
                    bfs(deque([(r, c)]))


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "T":
                    board[r][c] = "O"


