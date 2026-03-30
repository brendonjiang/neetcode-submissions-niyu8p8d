class Solution:
    def isHappy(self, n: int) -> bool:
        mySet = set()
        while True:
            n = str(n)
            total = 0
            for char in n:
                total += int(char)**2

            if total == 1:
                break

            if total in mySet:
                return False
            
            mySet.add(total)
            n = total
            

        
        return True