class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m-1, m+n-1, n-1


        while i >= 0 and k >= 0:
            if nums1[i] >= nums2[k]:
                nums1[j] = nums1[i] 
                i -= 1
                

            elif nums2[k] > nums1[i]:
                nums1[j] = nums2[k]
                k -= 1

            j -= 1

        
        while i >= 0:
            nums1[j] = nums1[i]
            i -= 1
            j -= 1

        while k >= 0:
            nums1[j] = nums2[k]
            k -= 1
            j -= 1

        