class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        visits = set()

        def dfs(i, r, c, visits):
            if i >= len(word) or min(r, c) < 0 or r == rows or c == cols or (r, c) in visits or board[r][c] != word[i]:
                return False
            
            if i == len(word)-1:
                return True

            visits.add((r, c))
            
            res = dfs(i+1, r+1, c, visits) or dfs(i+1, r-1, c, visits) or dfs(i+1, r, c+1, visits) or dfs(i+1, r, c-1, visits)
            visits.remove((r, c))

            return res


        starting_letter = word[0]


        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == starting_letter:
                    if dfs(0, r, c, visits):
                        return True


        return False