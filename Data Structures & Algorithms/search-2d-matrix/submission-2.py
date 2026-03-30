class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1

        while L <= R:
            m = (L+R)//2

            if target < matrix[m][0]:
                R = m-1

            elif target > matrix[m][-1]:
                L = m+1

            else:
                break

        print(matrix[m])
        L, R = 0, len(matrix[m])-1
        

        while L <= R:
            M = (L+R)//2

            if target < matrix[m][M]:
                R = M-1

            elif target > matrix[m][M]:
                L = M+1

            else:
                return True


        return False