class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visits or image[r][c] != org_color:
                return

            image[r][c] = color
            visits.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return


        visits = set()
        org_color = image[sr][sc]

        dfs(sr, sc)

        return image