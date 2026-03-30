class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix)-1
        L_inner = 0
        R_inner = len(matrix[0])-1

        while L <= R:
            m = (L+R) // 2
            if target < matrix[m][0]:
                R = m-1
            elif target > matrix[m][-1]:
                L = m+1
            else:
                while L_inner <= R_inner:
                    m_inner = (L_inner+R_inner) // 2
                    if target < matrix[m][m_inner]:
                        R_inner = m_inner-1
                    elif target > matrix[m][m_inner]:
                        L_inner = m_inner+1
                    else:
                        return True
                return False
        return False