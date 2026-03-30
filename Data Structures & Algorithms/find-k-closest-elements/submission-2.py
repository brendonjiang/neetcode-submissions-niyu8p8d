class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        L, R = 0, len(arr)-1

        while L < R and R-L+1 > k:
            left = abs(arr[L] - x)
            right = abs(arr[R] - x)


            if right > left:
                R -= 1
            
            elif left > right:
                L += 1

            else:
                R -= 1

        
        return arr[L:R+1]