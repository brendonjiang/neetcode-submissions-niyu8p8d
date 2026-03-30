class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True

        def helper(j, i):
            if i >= len(s):
                if i == j:
                    res.append(curset.copy())
                return
            
            
            
            if isPalindrome(s, j, i):
                curset.append(s[j:i+1])
                helper(i+1, i+1)
                curset.pop()

            
            helper(j, i+1)

        res, curset = [], []
        helper(0, 0)
        
        return res
            