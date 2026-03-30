class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
    
        L, R = 0, len(A)-1

        while True:
            m = (L+R) // 2
            m2 = half - m-2

            Aleft = A[m] if m >= 0 else float("-infinity")
            Aright = A[m+1] if (m+1) < len(A) else float("infinity")
            Bleft = B[m2] if m2 >= 0 else float("-infinity")
            Bright = B[m2+1] if (m2+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)

                else:
                    return (max(Aleft, Bleft)+min(Aright, Bright))/2

            elif Aleft > Bright:
                R = m-1
            else:
                L = m+1

                


        
                 