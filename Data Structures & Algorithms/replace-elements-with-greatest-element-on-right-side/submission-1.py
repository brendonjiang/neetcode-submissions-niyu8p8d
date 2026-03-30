class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        reverse_max = -1
        ans = [0]*len(arr)
        for i in range(len(arr)-1, -1, -1):
            
            ans[i] = reverse_max
            reverse_max = max(reverse_max, arr[i])
        
        return ans