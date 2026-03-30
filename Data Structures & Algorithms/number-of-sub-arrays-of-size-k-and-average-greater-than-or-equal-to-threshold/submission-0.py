class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        avg = 0
        total = 0
        L = 0
        count = 0
        window = set()

        for R in range(len(arr)):
            if R-L+1 > k:
                total -= arr[L]
                L += 1

            total += arr[R]

            if R-L+1 == k:
                avg = total / k

                if avg >= threshold:
                    count += 1

        return count
            