class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows, cols = len(board), len(board[0])
        visited = set()

        def helper(i, r, c):
            if i == len(word):
                return True

            if min(r, c) < 0 or r == rows or c == cols or word[i] != board[r][c] or (r, c) in visited:
                return False

            visited.add((r, c))

            res = helper(i+1, r+1, c) or helper(i+1, r-1, c) or helper(i+1, r, c+1) or helper(i+1, r, c-1)

            visited.remove((r, c))
            return res




        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if helper(0, r, c):
                        return True

        return False
