class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(cur, closed, opened):
            if closed == n and opened == n:
                res.append("".join(cur.copy()))
                return

            if opened < n:
                cur.append("(") 
                helper(cur, closed, opened+1)
                cur.pop()

            if closed < opened:
                cur.append(")")
                helper(cur, closed+1, opened)
                cur.pop()


        res = []
        helper([], 0, 0)

        return res