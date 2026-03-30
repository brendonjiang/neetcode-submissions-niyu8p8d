class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        L, R = 0, len(s)-1

        while L < R:
            if not s[L].isalpha() and not s[L].isnumeric():
                L += 1
                continue

            if not s[R].isalpha() and not s[R].isnumeric():
                R -= 1
                continue

            if s[R].lower() != s[L].lower():
                return False
            else:
                L += 1
                R -= 1
            
        return True
